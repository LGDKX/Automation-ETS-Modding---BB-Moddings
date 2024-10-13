# Import os in order to interact with Operation System
import os
# Import shutil to operate on folder and files
import shutil

# Get the path to the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the names of the folders to be copied
folders_to_copy = ['in', 'out']

# List of subfolder names
subfolder_names = [
    'agregados', 'agro', 'agronord', 'aria_fd_albg', 'aria_fd_esbj', 'aria_fd_jnpg',
    'aria_fd_trbg', 'aria_nordic', 'baltomors_ru', 'baltomorsk', 'batisse', 'batisse_base',
    'batisse_hs', 'batisse_road', 'cantera', 'canteras_ds', 'casa_olivera', 'cemelt_bas',
    'cemelt_fl_ru', 'cemelt_fla', 'cemelt_hal', 'concargo', 'cont_port', 'cont_port_fr',
    'cont_port_it', 'cont_port_ru', 'costruzi_bas', 'costruzi_fla', 'costruzi_hal',
    'dobr_ferm_bg', 'domdepo', 'domdepo_ru', 'egres', 'elcano_fla', 'engeron', 'euroacres',
    'euroacres_ru', 'eviksi', 'eviksi_a', 'fattoria_f', 'fui', 'huerta', 'iberatomica', 'in',
    'itcc', 'kivi', 'konstnr', 'konstnr_br', 'konstnr_hs', 'low_field', 'lvr', 'marina',
    'marina_fr', 'marina_it', 'marmo', 'ms_stein', 'mvm_carriere', 'nbfc', 'nord_sten',
    'nos_pat', 'nos_pat_brg', 'nos_pat_cf', 'nos_pat_lhv', 'nucleon', 'onnelik', 'onnelik_a',
    'ortiz', 'out', 'piac', 'quadrelli', 'quarry', 'quarrybr', 'rimaf', 'rock_eater', 'rt_log',
    'sanbuilders', 'severoatm_ru', 'tdc_auto', 'trainfoundry', 'tree_et', 'ts_atlas', 'ukko',
    'uko_zap', 'vitas_pwr', 'vitas_pwr_co', 'volvo_fac', 'wgcc', 'zelenye', 'zelenye_a'
]

# Path to the new folder on the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
new_folder_path = os.path.join(desktop_path, "NewFolder")

# Create the new folder on the desktop
os.makedirs(new_folder_path, exist_ok=True)

# Iterate through each subfolder name
for subfolder_name in subfolder_names:
    # Create the subfolder path
    subfolder_path = os.path.join(new_folder_path, subfolder_name)
    os.makedirs(subfolder_path, exist_ok=True)
    
    # Copy each folder from 'folders_to_copy' to the current subfolder
    for folder in folders_to_copy:
        folder_path = os.path.join(script_directory, folder)
        destination_path = os.path.join(subfolder_path, folder)
        
        if os.path.exists(folder_path):
            shutil.copytree(folder_path, destination_path)

print("Copy operation completed.")
