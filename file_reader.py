import glob, ndjson, sys
import pandas as pd

datatype_dict = {'text': str,'str': str, 'string': str, 'boolean': bool, 'bool': bool, 'integer': int, 'int':int, 'float': float}

        
def read_file(filename, out_filename, specs):
    out = ndjson.writer(open(out_filename, 'w'), ensure_ascii=False)
    for lines in open(filename, 'r').readlines():
        temp_dict = []
        for index, row in specs.iterrows():
            if index==0:
                temp_dict.append((row['column name'], row['datatype'](lines[0:specs['width'].iloc[index]].strip())))
            else:
                if row['datatype'] is bool:
                    temp_dict.append((row['column name'], row['datatype'](int(lines[specs['width'].iloc[index-1]:specs['width'].iloc[index]]))))
                else:
                    temp_dict.append((row['column name'], row['datatype'](lines[specs['width'].iloc[index-1]:specs['width'].iloc[index]])))
        
        print(dict(temp_dict))
        out.writerow(dict(temp_dict))
    


def create_spec(file_specs):
    try:
        for i, val in file_specs.iterrows():
            if i==0:
                continue
            else:
                file_specs.at[i, 'width'] = file_specs['width'].iloc[i-1] + file_specs['width'].iloc[i]

        file_specs['datatype'] = file_specs['datatype'].apply(lambda x: datatype_dict[x.lower().strip()])
        # print(file_specs)
        print(file_specs['datatype'], datatype_dict)
    except KeyError as k:
        print(f'Key not found in filespecs or data type {k}')
        exit()
    except Exception as e:
        print(f'Exception Occured while modifying specs file {e}')
        exit()

    try:
        ######### Get all the data files ##########
        all_files = glob.glob('./data/'+filename+'_*.txt')
        if len(all_files)==0:
            print(f'data file ./specs/ {filename}.txt not found')
            exit()
        for files in all_files:
            print(files)
            out_filename_root = files.strip().split('/')[1].split('.')[0]
            out_filename = './out/'+out_filename_root+'.ndjson'
            print(out_filename)
            read_file(files, out_filename, file_specs)

    except FileNotFoundError as e:
        print(f'data file ./specs/ {filename}.txt not found')
    except Exception as e:
        print(f"Exception occured while parsing data file {e}")


def main(filename):
    ### Read the Specifications #######
    try:
        file_specs = pd.read_csv('./specs/'+filename+'.csv')
        create_spec(file_specs)
    except FileNotFoundError as e:
        print(f'specs file ./specs/ {filename}.csv not found')
        exit()
    except Exception as e:
        print(f"Exception occured while reading specs file {e}")
        exit()

if __name__ == '__main__': 
    try:
        filename = sys.argv[1]
        filename = filename.strip().split('.')[0]
        main(filename)
    except IndexError as e:
        print(f'Sys argument not provided for filename, command to run the script "Python file_reader.py **filename**"')
        exit()
    except Exception as e:
        print(f'Exception occured while getting the base filename {e}')
        exit()
