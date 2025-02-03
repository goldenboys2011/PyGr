import sys
import os
import re
import requests
import shutil

app_version = 1.1
version_url = "https://raw.githubusercontent.com/goldenboys2011/PyGr/refs/heads/main/update/version.json"
update_url = "https://raw.githubusercontent.com/goldenboys2011/PyGr/refs/heads/main/update/pygrRunner.py"


translation_dict = {
    # Variables
    'ακέραιος_μεταβλητή': 'integer_var',
    'ακεραιος_μεταβλητή': 'integer_var',
    'δεκαδικός_μεταβλητή': 'float_var',
    'δεκαδικος_μεταβλητή': 'float_var',
    'συμβολοσειρά_μεταβλητή': 'string_var',
    'συμβολοσειρα_μεταβλητή': 'string_var',
    'λογική_μεταβλητή': 'boolean_var',
    'λογικη_μεταβλητή': 'boolean_var',
    'λίστα_μεταβλητή': 'list_var',
    'λιστα_μεταβλητή': 'list_var',
    'πλειάδα_μεταβλητή': 'tuple_var',
    'πλειαδα_μεταβλητή': 'tuple_var',
    'σύνολο_μεταβλητή': 'set_var',
    'συνολο_μεταβλητή': 'set_var',
    'λεξικό_μεταβλητή': 'dict_var',
    'λεξικο_μεταβλητή': 'dict_var',

    # Keywords
    'ανάστροφα': 'reverse',
    'αναστροφα': 'reverse',
    'εάν': 'if',
    'εαν': 'if',
    'αλλιώς': 'else',
    'αλλιως': 'else',
    'τύπος': 'type',
    'τυπος': 'type',
    'για': 'for',
    'ενώ': 'while',
    'ενω': 'while',
    'προσπάθεια': 'try',
    'προσπαθεια': 'try',
    'εκτός': 'except',
    'εκτος': 'except',
    'με': 'with',
    'ως': 'as',
    'από': 'from',
    'απο': 'from',
    'εισαγωγή': 'import',
    'εισαγωγη': 'import',
    'κλάση': 'class',
    'κλαση': 'class',
    'ορισμός': 'def',
    'ορισμος': 'def',
    'επιστροφή': 'return',
    'επιστροφη': 'return',
    'εκτύπωσε': 'print',
    'εκτυπωσε': 'print',
    'άνοιξε': 'open',
    'ανοιξε': 'open',
    'λ': 'lambda',
    'εύρος': 'range',
    'ευρος': 'range',
    'απόδοση': 'yield',
    'αποδοση': 'yield',
    'Αληθές': 'True',
    'Αληθες': 'True',
    'Ψευδές': 'False',
    'Ψευδες': 'False',
    'αληθές': 'True',
    'αληθες': 'True',
    'ψευδές': 'False',
    'ψευδες': 'False',
    'απόσταση': 'range',
    'αποσταση': 'range',
    'σε': 'in',
    'γύρος': 'round',
    'γυρος': 'round',
    'εισαγωγή': 'input',
    'εισαγωγη': 'input',
    'ακέραιος': 'int',
    'ακεραιος': 'int',
    'μήκος': 'len',
    'μηκος': 'len',
    'είναι_αλφαριθμητικό': 'isalnum',
    'ειναι_αλφαριθμητικο': 'isalnum',
    'κεφαλαιοποίηση': 'capitalize',
    'κεφαλαιοποιηση': 'capitalize',

    # Additional built-in functions
    'απόλυτος': 'abs',
    'απολυτος': 'abs',
    'όλα': 'all',
    'ολα': 'all',
    'οποιοδήποτε': 'any',
    'οποιοδηποτε': 'any',
    'αριθμητική': 'bin',
    'αριθμητικη': 'bin',
    'λογική_τιμή': 'bool',
    'λογικη_τιμη': 'bool',
    'εκτέλεση': 'exec',
    'εκτελεση': 'exec',
    'εύρος': 'range',
    'ευρος': 'range',
    'εξέταση': 'eval',
    'εξεταση': 'eval',
    'μήκος': 'len',
    'μηκος': 'len',
    'μέγιστος': 'max',
    'μεγιστος': 'max',
    'ελάχιστος': 'min',
    'ελαχιστος': 'min',
    'άθροισμα': 'sum',
    'αθροισμα': 'sum',
    'διάταξη': 'sorted',
    'διαταξη': 'sorted',
    'κείμενο': 'str',
    'κειμενο': 'str',
    'τιμή': 'value',
    'τιμη': 'value',
    'μήνυμα': 'message',
    'μηνυμα': 'message',
    'διαμόρφωση': 'format',
    'διαμορφωση': 'format',
    'σημείωση': 'note',
    'σημειωση': 'note',
    'αριθμός': 'number',
    'αριθμος': 'number',
    'φίλτρο': 'filter',
    'φιλτρο': 'filter',
    'χάρτης': 'map',
    'χαρτης': 'map',
    'συμμετέχων': 'participant',
    'συμμετεχων': 'participant',
    'κατάσταση': 'state',
    'κατασταση': 'state',
    'εφαρμογή': 'apply',
    'εφαρμογη': 'apply',
    'παράδειγμα': 'example',
    'παραδειγμα': 'example',
    'περιγραφή': 'description',
    'περιγραφη': 'description',
    'ρυθμίσεις': 'settings',
    'ρυθμισεις': 'settings',
    'εντολή': 'command',
    'εντολη': 'command',
    'διακοπή': 'break',
    'διακοπη': 'break',
    'συνέχεια': 'continue',
    'συνεχεια': 'continue',
    
    'και': 'and',
    'η': 'or',
    'όχι': 'not',
    'οχι': 'not',
    'είναι': 'is',
    'ειναι': 'is',
    'κανένα': 'None',
    'κανενα': 'None',
    'περάστε': 'pass',
    'περαστε': 'pass',
    'τελεία': 'ellipsis',
    'τελεια': 'ellipsis',
    'δημόσιο': 'global',
    'δημοσιο': 'global',
    'μη_τοπικό': 'nonlocal',
    'μη_τοπικο': 'nonlocal',
    'διεκδίκηση': 'assert',
    'διεκδικηση': 'assert',
    'ανύψωση': 'raise',
    'ανυψωση': 'raise',
    'διαγράψτε': 'del',
    'διαγραψτε': 'del',
    'παράλειψη': 'pass',
    'παραλειψη': 'pass',
    
    'δεκαδικός': 'float',
    'δεκαδικος': 'float',
    'περίπου': 'round',
    'περιπου': 'round',
    'διαιρεση': 'divmod',
    'διαιρεση': 'divmod',
    'χαρακτήρας': 'chr',
    'χαρακτηρας': 'chr',
    'κωδικός': 'ord',
    'κωδικος': 'ord',
    'έκτυπος': 'repr',
    'εκτυπος': 'repr',
    'δύναμη': 'pow',
    'δυναμη': 'pow',
    'άθροισμα': 'sum',
    'αθροισμα': 'sum',
    'ανοιχτό': 'open',
    'ανοιχτο': 'open',
    'ενώνει': 'join',
    'ενωνει': 'join',
    'μετράει': 'count',
    'μετραει': 'count',
    'αντιστρέφει': 'reversed',
    'αντιστρεφει': 'reversed',
    'κόβει': 'slice',
    'κοβει': 'slice',
    'στρογγυλοποίηση': 'round',
    'στρογγυλοποιηση': 'round',
    'διαίρεση': 'divmod',
    'διαιρεση': 'divmod'


}


def translate_to_python(greek_code):
    segments = re.split(r'(\".*?\"|\'.*?\')', greek_code)
    
    translated_segments = []
    for segment in segments:
        if segment.startswith('"') or segment.startswith("'"):
            translated_segments.append(segment)
        else:
            for gr_keyword, en_keyword in translation_dict.items():
                segment = re.sub(r'\b' + gr_keyword + r'\b', en_keyword, segment)
            translated_segments.append(segment)
    
    return ''.join(translated_segments)

def run_translated_code(code):
    exec(code, globals())

def download_and_replace():
    try:
        print("Downloading update...")
        response = requests.get(update_url, stream=True, timeout=10)
        response.raise_for_status()

        #file_size = int(response.headers.get("content-length", 0))
        #if file_size < 10000:
            #print("Update file seems too small. Aborting update.")
            #return
        
        # For Python File
        with open("pygrRunner.py", "w", encoding="utf-8") as file:
            file.write(response.text)

        # For builded file
      # with open("pygrRunner.exe", "wb") as file:
      #     shutil.copyfileobj(response.raw, file)
    
        print("Update downloaded successfully.")

        shutil.move("pygrRunner.py", sys.argv[0])
        print("Update applied successfully! Restarting...")
        
        os.execv(sys.argv[0], sys.argv)
        sys.exit(1)

    except Exception as e:
        print(f"Update failed: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python translate_and_run.py <script.pygr>")
        sys.exit(1)
    
    script_path = sys.argv[1]
    
    if script_path.startswith("--") and not script_path.endswith(".pygr"):
        if script_path == "--update" or script_path == "--u":
            update = input("Would you like to update the software now? (Y/N) ")
            
            while update != "Y" and update != "N":
                update = input("Would you like to update the software now? (Y/N) ")
            
            if update == "N":
                print("Understanable. Have a great day!")
                sys.exit(1)
            else:
                print("Checking for updates")
                response = requests.get(version_url, timeout=5)
                response.raise_for_status()
                latest_version = response.json().get("v", app_version)

                if latest_version > app_version:
                    print(f"Update Found! Downloading version {latest_version}")
                    download_and_replace()
                else:
                    print("You have got the latest version of PyGR")
                    sys.exit(1)
                    
    if not os.path.isfile(script_path):
        print(f"File {script_path} not found. Current directory: {os.getcwd()}")
        sys.exit(1)

    try:
        with open(script_path, 'r', encoding='utf-8') as file:
            greek_code = file.read()
    except Exception as e:
        print(f"Error reading file {script_path}: {e}")
        sys.exit(1)
    
    translated_code = translate_to_python(greek_code)
    run_translated_code(translated_code)

if __name__ == "__main__":
    main()
