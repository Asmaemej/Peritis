"""
==========
Partie Python
Exercice 1
==========

"""

def read_file(filename) :
    """
    read a text file

    :param filename: The name of the file to be read
    :return: A list containing the lines of the file as elements.
    """
    with open(filename) as f:
        text = f.read().split('\n')
    return text


def write_to_file(filename, text):
    """
    write to a file

    :param filename: The name of the file to write to
    :param text: The text (e.g., an IP address) to be written to the file.
    :return: 
    """
    with open(filename, 'a') as f:
        f.write(text + '\n')

        
def check(ip):
    """
    This function is used to check if the given IP address is valid
    
    :param ip: The ip adress
    :return: Boolean indicating whether the IP address is valid
    """
    is_valid = False
    if "." in ip:
        ip_list = ip.split('.')
        if len(ip_list) == 4:
            if all(0 < len(elmt) < 4 and 0 <= int(elmt) <= 255 for elmt in ip_list):
                is_valid = True
    return is_valid

#Or we can simply use ipadress library

if __name__ == '__main__':
    input_filename = "Input.txt"
    correct_ips_filename = 'correct_ips.txt'
    incorrect_ips_filename = 'incorrect_ips.txt'

    ip_list = read_file(input_filename)
    
    for ip_adress in ip_list:
        if check(ip_adress):
            write_to_file(correct_ips_filename, ip_adress)
        else:
            write_to_file(incorrect_ips_filename, ip_adress)