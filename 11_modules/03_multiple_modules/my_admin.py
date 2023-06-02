from admin import Admin
from admin import Privilege

my_admin = Admin('Erika', 'Flores', 'Daedra', [Privilege('can_read')])
my_admin.add_privilege(Privilege('can_delete'))
my_admin.add_privilege(Privilege('can_edit'))

print(my_admin.descriptive_user())
my_admin.print_privilege()
