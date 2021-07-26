# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    numbers.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hcho <hcho@student.42seoul.kr>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 16:44:59 by hcho              #+#    #+#              #
#    Updated: 2021/07/26 23:35:49 by hcho             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def numbers():
    try:
        filename = open("numbers.txt", 'r')
    except:
        exit()
    else:
        for i in filename.readline().rstrip("\n").split(","):
            print(i)
        filename.close()

if __name__ == '__main__':
    numbers()
