from django import template
from django.utils.safestring import mark_safe
#from mainapp.models import Prod2

register = template.Library()

TABLE_HEAD = """
                <table class="table">
                  <tbody>
             """

TABLE_TAIL = """
                  </tbody>
                </table>
             """


TABLE_CONTENT = """
                    <tr>
                      <td>{name}</td>
                      <td>{value}</td>
                    </tr>
                """


# PRODUCT_SPEC = {
#     'prod1': {
#         'Характеристика 1': 'spec1',
#         'Характеристика 2': 'spec2',
#         'Характеристика 3': 'spec3',
#
#     },
#     'prod2': {
#         'Характеристика 1': 'spec1',
#         'Характеристика 2': 'spec2',
#         'Характеристика 3': 'spec3',
#
#     }
# }














# def get_product_spec(product, model_name):
#     table_content = ''
#     for name, value in PRODUCT_SPEC[model_name].items():
#         table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
#     return table_content
#
#
# @register.filter
# def product_spec(product):
#     model_name = product.__class__._meta.model_name
#     if isinstance(product, Prod2):
#         if not product.sd:
#             PRODUCT_SPEC['prod2'].pop('', None)
#         else:
#             PRODUCT_SPEC['prod2'][''] = ''
#     return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)


