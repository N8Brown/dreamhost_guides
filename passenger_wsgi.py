import sys, os

INTERP = "<python_interpreter_path_here>" #See Guide: Template - Section 1 
 
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv) #INTERP is present twice so that the new python interpreter knows the actual executable path

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/<django_project_name_here>')  #See Guide: Template - Section 2

sys.path.insert(0,cwd+'/<virtual_environment_name_here>/bin') #See Guide: Template - Section 3
sys.path.insert(0,cwd+'/<virtual_environment_name_here>/lib/<python_version_directory_name_here>/site-packages') #See Guide: Template - Section 4

os.environ['DJANGO_SETTINGS_MODULE'] = "<django_project_name_here>.settings" #See Guide: Template - Section 5
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
