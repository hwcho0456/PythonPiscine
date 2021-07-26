# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    periodic_table.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hcho <hcho@student.42seoul.kr>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 23:21:19 by hcho              #+#    #+#              #
#    Updated: 2021/07/27 04:23:03 by hcho             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def periodic_table():
    try:
        filename = open("periodic_table.txt", 'r')
    except:
        exit()
    else:
        elements = []
        while True:
            line = filename.readline()
            if not line:
                break
            data = []
            info = line.replace('=', ',').split(',')
            for i in info:
                data.append(i.split(':')[-1].strip())
            elements.append(data)
        filename.close()
        try:
            html = open("periodic_table.html", 'w')
        except:
            filename.close()
            exit()
        else:
            fam = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII"]
            form = "<style> \
                    {margin:0;padding:0;box-sizing:border-box;} \
                    body{margin:0 auto;width:100%;} \
                    ul{padding-left:0px;text-align:center;} \
                    li{list-style:none;font-size:14px;} \
                    table{margin:0 auto; border-collapse:collapse;} \
                    td{min-width:120px;border:1px solid black;padding:5px;} \
                    .nonmetal{background-color:#e7ff8f;} \
                    .noble{background-color:#c0ffff} \
                    .alkali{background-color:#ff6666;} \
                    .earth{background-color:#ffdead;} \
                    .transit{background-color:#ffc0c0;} \
                    .post{background-color:#cccccc;} \
                    .metalloid{background-color:#cccc99;} \
                    .none{background-color:#eeeeee;} \
                    .dummy{border:0;} \
                    .left{min-width:10px;text-align:center;border:0;} \
                    h1{text-align: left; font-size:40px; margin: 20px 120px;} \
                    h4{text-align: center;font-size:36px;margin:0px;padding: 0px;} \
                    h5{text-align: left;font-size:20px;margin:0px;padding:0px;} \
                    .top{text-align: center; border:0;} \
                    </style> \
                    <h1>Periodic Table</h1> \
                    <table><tr>"
            for i in fam:
                form += "<td class=\"top\"><h2>"+i+"</h2></td>"
            form += "</tr>"
            pos = 0
            per = 1
            for element in elements:
                kind = "post"
                if int(element[1]) <= 10:
                    kind = 'transit'
                if int(element[1]) == 0:
                    kind = 'alkali'
                if int(element[1]) == 1:
                    kind = 'earth'
                if int(element[2]) == 1 or (int(element[1])-per <= 16 and int(element[1])-per >= 10):
                    kind = 'nonmetal'
                if int(element[2]) == 32 or int(element[2]) == 51 or int(element[1])-per == 9:
                    kind = 'metalloid'
                if int(element[1]) == 17:
                    kind = 'noble'
                if int(element[2]) >= 109 and int(element[2]) != 112:
                    kind = 'non'
                if pos == 0:
                    form += "<tr><td class=\"left\"><h2>"+str(per)+"</h2></td>"
                    per += 1
                while int(element[1]) != pos:
                    form += "<td class=\"dummy\"></td>"
                    pos += 1
                form += "<td class=\""+kind+"\"> \
                            <h5>"+element[2]+"</h5> \
                            <h4>"+element[3]+"</h4> \
                            <ul> \
                                <li style=\"font-size:20px;\">"+element[0]+"</li> \
                                <li style=\"font-size:16px;\">"+element[4]+"</li> \
                                <li>"+element[5]+"</li> \
                            </ul> \
                        </td>"
                pos += 1
                if pos == 18:
                    pos = 0
                    form += "</tr>"
            form += "</table>"
            html.write(form)
            html.close()

if __name__ == '__main__':
    periodic_table()
