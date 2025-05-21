import os
import importlib
import sys

# Check Python version
print(f"Python version: {sys.version}")

# Check if certificate_generator.py exists
cert_gen_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'certificate_generator.py')
print(f"Certificate generator file exists: {os.path.exists(cert_gen_path)}")

# Try to import the module
try:
    import certificate_generator
    print("Successfully imported certificate_generator module")
    
    # Check if generate_certificate function exists
    if hasattr(certificate_generator, 'generate_certificate'):
        print("generate_certificate function exists in the module")
    else:
        print("ERROR: generate_certificate function does not exist in the module")
        print("Available attributes:", dir(certificate_generator))
except ImportError as e:
    print(f"ERROR importing certificate_generator module: {e}")

# Check if templates directory exists
templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
print(f"Templates directory exists: {os.path.exists(templates_dir)}")

if os.path.exists(templates_dir):
    template_files = os.listdir(templates_dir)
    print("Template files found:", template_files)

# Check if required packages are installed
required_packages = ['flask', 'mysql.connector', 'reportlab']
for package in required_packages:
    try:
        importlib.import_module(package)
        print(f"Package {package} is installed")
    except ImportError:
        print(f"ERROR: Package {package} is NOT installed")

print("\nIf you're seeing any errors above, please fix them before running app2.py again.")
print("If certificate_generator.py exists but the function is not found, make sure it has the correct content.")