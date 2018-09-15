class HDD :

    '''A base/main class to discribe HDD properties'''

    main_counter=0 

    def __init__(self, firm_name, model_name, serial_number,firmware_version, product_date):
        self.new_hdd={}
        self.new_hdd['firm_name']=firm_name or 'zzz'
        self.new_hdd['model_name']=model_name or 'zzz'
        self.new_hdd['serial_number']=serial_number or 'zzz'
        self.new_hdd['firmware_version']=firmware_version or 'zzz'
        self.new_hdd['product_date']=product_date or 'zzz'
        # self.sound = chat
        HDD.main_counter += 1
        self.new_hdd['index']=HDD.main_counter


    def get_info(self) :
        return self.new_hdd

    # def get_index(self):
    #     return self.index


