"""Constants for the Divergent Discourses Corpus Analysis Tools"""

# Newspaper codes and full names
NEWSPAPER_NAMES = {
    'CWN': 'Central Weekly News (krung dbyang gsar \'gyur)',
    'DTF': 'Defend Tibet\'s Freedom (rang dbang srung skyob gsar shog)',
    'FRD': 'Freedom (rang dbang gsar shog)',
    'GDN': 'Ganze Daily (dkar mdzes nyin re\'i gsar \'gyur)',
    'GOT': 'Understanding (go rtogs)',
    'GTN': 'Gyantse News (rgyal rtse gsar \'gyur)',
    'KDN': 'Kangding News (dar mdo\'i gsar \'gyur)',
    'MJN': 'Minjiang News (min kyang tshags dpar)',
    'NIB': 'News in Brief (gsar \'gyur mdor bsdus)',
    'QTN': 'Qinghai Tibetan News (mtsho sngon bod yig gsar \'gyur)',
    'SGN': 'South Gansu News (kan lho gsar \'gyur)',
    'TDP': 'Tibet Daily Pictorial (bod ljongs nyin re\'i gsar \'gyur par ris)',
    'TID': 'Tibet Daily (bod ljongs nyin re\'i gsar \'gyur)',
    'TIF': 'Tibetan Freedom (bod mi\'i rang dbang)',
    'TIM': 'Tibet Mirror (yul phyog so so\'i gsar \'gyur me long)',
    'XNX': 'South-West Institute for Nationalities (lho nub mi rigs slob grwa chen po)',
    'ZYX': 'Central Institute for Nationalities (krung dbyang mi rigs slob grwa)'
}

# Enhanced metadata about newspapers
NEWSPAPER_METADATA = {
    'CWN': {'region': 'India', 'publisher': 'KMT', 'type': 'Political'},
    'DTF': {'region': 'India', 'publisher': 'CTA', 'type': 'Political'},
    'FRD': {'region': 'India', 'publisher': 'CTA', 'type': 'General'},
    'GDN': {'region': 'PRC', 'publisher': 'State', 'type': 'General', 'level': 'Prefectural', 'province': 'Sichuan'},
    'GOT': {'region': 'Nepal', 'publisher': 'Guerrilla', 'type': 'Military'},
    'GTN': {'region': 'PRC', 'publisher': 'State', 'type': 'General', 'level': 'County', 'province': 'TAR'},
    'KDN': {'region': 'PRC', 'publisher': 'State', 'type': 'General', 'level': 'Prefectural', 'province': 'Xikang/Sichuan'},
    'MJN': {'region': 'PRC', 'publisher': 'State', 'type': 'General', 'level': 'Prefectural', 'province': 'Sichuan'},
    'NIB': {'region': 'PRC', 'publisher': 'State', 'type': 'General', 'level': 'Provincial', 'province': 'TAR'},
    'QTN': {'region': 'PRC', 'publisher': 'State', 'type': 'General', 'level': 'Provincial', 'province': 'Qinghai'},
    'SGN': {'region': 'PRC', 'publisher': 'State', 'type': 'General', 'level': 'Prefectural', 'province': 'Gansu'},
    'TDP': {'region': 'PRC', 'publisher': 'State', 'type': 'Pictorial', 'level': 'Provincial', 'province': 'TAR'},
    'TID': {'region': 'PRC', 'publisher': 'State', 'type': 'General', 'level': 'Provincial', 'province': 'TAR'},
    'TIF': {'region': 'India', 'publisher': 'CTA', 'type': 'General'},
    'TIM': {'region': 'India', 'publisher': 'Independent', 'type': 'General'},
    'XNX': {'region': 'PRC', 'publisher': 'Educational', 'type': 'Institutional', 'level': 'Institutional'},
    'ZYX': {'region': 'PRC', 'publisher': 'Educational', 'type': 'Institutional', 'level': 'Institutional'},
}

# Library codes
LIBRARY_CODES = {
    'BD': 'Bodleian Library, Oxford',
    'BL': 'British Library, London',
    'CF': 'Collège de France, Paris',
    'CU': 'Columbia University, New York',
    'IT': 'University of Vienna',
    'LT': 'Library of Tibetan Works and Archives',
    'MV': 'Grassi Museum für Völkerkunde, Leipzig',
    'NC': 'National Chengchi University, Taipei',
    'OI': 'Oriental Institute, Prague',
    'RB': 'Private Collection (Robbie Barnett)',
    'SB': 'Staatsbibliothek zu Berlin',
    'TL': 'LTWA, Dharamshala',
    'TM': 'Tibet Museum',
    'TS': 'Private Collection (Tenzin Sonam)',
    'UW': 'University of Washington'
}

# Valid image file extensions
VALID_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.tif', '.tiff', '.pdf']

# Filename pattern for newspaper pages
FILENAME_PATTERN = r'^([A-Z]{3})_(\d{4})_(\d{2})_(\d{2})_(\d{3})_([A-Z]{2})(?:_(.+))?$'
