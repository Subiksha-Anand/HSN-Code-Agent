from agent import utils

class HSNAgent:
    def __init__(self, excel_path=r"C:\Users\subik\OneDrive\Document\PROJECT\hsn_agent_project\data\HSN_Master_Data.xlsx"):
        self.df = utils.load_hsn_data(excel_path)

    def validate_hsn_code(self, code):
        result = {'code': code, 'valid_format': False, 'exists': False, 'hierarchy': [], 'message': ''}
        
        if not utils.validate_format(code):
            result['message'] = 'Invalid format. Code must be numeric and 2/4/6/8 digits.'
            return result
        
        result['valid_format'] = True
        result['exists'] = utils.validate_existence(code, self.df)
        
        if result['exists']:
            description = self.df[self.df['HSNCode'] == code]['Description'].values[0]
            result['message'] = f'✅ Valid HSN Code: {code} - {description}'
            result['description'] = description
            
            # Check hierarchy
            result['hierarchy'] = [
                (parent, self.df[self.df['HSNCode'] == parent]['Description'].values[0])
                for parent in utils.get_hierarchy_codes(code)
                if parent in self.df['HSNCode'].values
            ]
        else:
            result['message'] = '❌ Code not found in dataset.'
        
        return result

    def suggest_from_description(self, desc):
        return utils.suggest_hsn(desc, self.df)
