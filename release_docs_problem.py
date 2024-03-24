list_sample = ['1','1.0','1.0.3', '2.10', '5.10', '1.0.0', '2.0.19', '3.1']

def solution(list_q):
    release_dict = {}
    for v in list_q:
        values = list(map(int, v.strip().split('.')))
        print('values', values)
        if values[0] not in release_dict.keys():
            release_dict[values[0]] = {}
        print('release dict values', release_dict)
        if len(values)<2:
            if -1 not in release_dict[values[0]].keys():
                release_dict[values[0]][-1] = {}
        else:
            if values[1] not in release_dict[values[0]].keys():
                release_dict[values[0]][values[1]] = {}
        
        if len(values)<3:
            if len(values)<2:
                continue
            elif -1 not in release_dict[values[0]][values[1]].keys():
                release_dict[values[0]][values[1]][-1] = {}
        else:
            if values[2] not in release_dict[values[0]][values[1]].keys():
                release_dict[values[0]][values[1]][values[2]] = {}

    sorted_list = []
    sorted_keys = sorted(release_dict.keys())
    print('sorted', sorted_keys)
    for keys in sorted_keys:
        print('keys', keys)
        key_values = release_dict[keys].keys()
        ltl_final_value = str(keys)
        sorted_key_value =  (key_values)
        print('final value', ltl_final_value)
        for key_value in sorted_key_value:
            new_sorted_key_value = sorted(release_dict[keys][key_value].keys())
            # print(new_sorted_key_value, sorted_key_value, keys)
            print("key value", key_value, new_sorted_key_value)
            if key_value != -1:
                last_final_value= ltl_final_value + '.'+ str(key_value)
                print('final value', last_final_value)
            else:
                print('final value', ltl_final_value)
                sorted_list.append(ltl_final_value)
            
            for v in new_sorted_key_value:
                print('v',v)
                if v!=-1:
                    final_value = last_final_value + '.' + str(v)
                    print('final value', final_value)
                    sorted_list.append(final_value)
                else:
                    sorted_list.append(last_final_value)

                
                
    print('sorted list', sorted_list)
        
        

        
    print("release dict", release_dict)

solution(list_sample)