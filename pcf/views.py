'''
views.py
'''
from flask import render_template, Blueprint
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm

from .main import app, db
from . import models
from .adminView import admin

pcf = Blueprint('pcf', __name__)

# 定義一基本的設定，可適用於其他的 modelview
class BaseModelView(ModelView):
    # 可用 Ajax 建立 models
    create_modal = False
    # 可用 Ajax 修改 models
    edit_modal = False
    # 可 export 資料
    can_export = True
    # 可看詳細資料，但會看到密碼
    # can_view_details = True
    # 加入 CSRF 驗證
    form_base_class = SecureForm
    # 顯示所有 one to many 和 many to many 的資料
    column_display_all_relations = True
    # 一頁顯示的個數
    page_size = 50


class ModelsView(BaseModelView):
    # 想顯示的資料
    column_list = ('JIRA', 'name', 'projectCode', 'stage', 'PM', 'APM',
                   'modelNameCode', 'remark', 'owner', 'productIDs')
    # 建立時可順便建立 one to many or many to many 的 relationship 資料
    inline_models = (models.ProductIDs, )

    def __init__(self, session, **kwargs):
        super().__init__(models.Models, session, **kwargs)


admin.add_view(ModelsView(db.session))


class ProductIDsView(BaseModelView):
    # 想顯示的資料
    column_list = ('name', 'model', 'customer', 'customerModelName',
                   'components', 'documents', 'histories')
    # 欲直接搜尋的資料
    column_searchable_list = ('name', 'customerModelName')
    # 欲篩選的資料
    column_filters = ('model', 'customer', 'components')
    # 建立時可順便建立 one to many or many to many 的 relationship 資料
    inline_models = (models.Components, models.Histories)

    def __init__(self, session, **kwargs):
        super().__init__(models.ProductIDs, session, **kwargs)


admin.add_view(ProductIDsView(db.session))


class ComponentsView(BaseModelView):
    # 想顯示的資料
    column_list = ('PN_number', 'name', 'type', 'vendor', 'remark',
                   'productIDs')
    # 欲直接搜尋的資料
    column_searchable_list = (models.Components.PN_number,
                              models.Components.name)
    # 欲篩選的資料
    column_filters = ('type', 'vendor')
    # 預設排列
    column_default_sort = 'type'

    def __init__(self, session, **kwargs):
        super().__init__(models.Components, session, **kwargs)


admin.add_view(ComponentsView(db.session))


class HistoriesView(BaseModelView):
    # 想顯示的資料
    column_list = ('date', 'type', 'PCBAs', 'PCBA_version', 'circuitVersion',
                   'PCBs', 'PCB_version', 'remark', 'productIDs', 'documents')
    # 欲直接搜尋的資料
    column_searchable_list = ('PCBAs', )
    # 欲篩選的資料
    column_filters = ('type', )
    # 建立時可順便建立 one to many or many to many 的 relationship 資料
    inline_models = (models.Documents, )

    def __init__(self, session, **kwargs):
        super().__init__(models.Histories, session, **kwargs)


admin.add_view(HistoriesView(db.session))


class DocumentsView(BaseModelView):
    # 想顯示的資料
    column_list = ('DN_number', 'type', 'stage', 'remark', 'productIDs',
                   'histories')
    # 欲直接搜尋的資料
    column_searchable_list = ('DN_number', )
    # 欲篩選的資料
    column_filters = ('type', 'stage')
    # 預設排列
    column_default_sort = 'type'

    def __init__(self, session, **kwargs):
        super().__init__(models.Documents, session, **kwargs)


admin.add_view(DocumentsView(db.session))


class OwnersView(BaseModelView):
    # 想顯示的資料
    column_list = ('name', 'models')

    def __init__(self, session, **kwargs):
        super().__init__(models.Owners, session, **kwargs)


admin.add_view(OwnersView(db.session))


@pcf.route('/', methods=["GET"])
def index():
    return render_template('index.html', title="總覽")
