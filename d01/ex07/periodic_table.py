#!/usr/bin/env python3

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
            fam = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII"]
            form = ("<!DOCTYPE html>\n" +
                    "<html lang=\"en\">" +
                    "<head>\n" +
                    "   <meta charset=\"UTF-8\">\n" +
                    "   <title>Periodic_Table</title>\n" +
                    "   <style>\n" +
                    "       *{margin:0;padding:0;box-sizing:border-box;}\n" + 
                    "       body{margin:0 auto;width:100%;}\n" +
                    "       ul{padding-left:0px;text-align:center;}\n" +
                    "       li{list-style:none;font-size:14px;}\n" +
                    "       li h4{font-size:20px;}\n" +
                    "       table{margin:0 auto; border-collapse:collapse;}\n" +
                    "       td{min-width:150px;border:1px solid black;padding:5px;}\n" +
                    "       .nonmetal{background-color:#e7ff8f;}\n" +
                    "       .noble{background-color:#c0ffff}\n" +
                    "       .alkali{background-color:#ff6666;}\n" +
                    "       .earth{background-color:#ffdead;}\n" +
                    "       .transit{background-color:#ffc0c0;}\n" +
                    "       .post{background-color:#cccccc;}\n" +
                    "       .metalloid{background-color:#cccc99;}\n" +
                    "       .none{background-color:#eeeeee;}\n" +
                    "       .top{text-align: center; border:0;}\n" +
                    "       .dummy{border:0;}\n" +
                    "       .left{min-width:30px;border:0;padding:20px;}\n" +
                    "       h1{font-size:40px; margin: 20px 80px;}\n" +
                    "       h4{text-align: center;font-size:36px;}\n" +
                    "       h5{font-size:20px;}\n" +
                    "   </style>\n" +
                    "</head>\n" +
                    "<body>\n" +
                    "   <h1>Periodic Table</h1>\n" +
                    "   <table>\n" +
                    "       <tr>\n" +
                    "          <td class=\"left\">\n" +
                    "          </td>\n")
            for i in fam:
                form += ("          <td class=\"top\">\n" +
                         "              <h2>"+i+"</h2>\n" +
                         "          </td>\n")
            form += "       </tr>\n"
            pos = 0
            per = 1
            for element in elements:
                kind = "post"
                if int(element[1]) <= 10:
                    kind = "transit"
                if int(element[1]) == 0:
                    kind = "alkali"
                if int(element[1]) == 1:
                    kind = "earth"
                if int(element[2]) == 1 or (int(element[1]) - per <= 16 and int(element[1]) - per >= 10):
                    kind = "nonmetal"
                if int(element[2]) == 32 or int(element[2]) == 51 or int(element[1]) - per == 9:
                    kind = "metalloid"
                if int(element[1]) == 17:
                    kind = "noble"
                if int(element[2]) >= 109 and int(element[2]) != 112:
                    kind = "non"
                if pos == 0:
                    form += ("      <tr>\n" + 
                             "          <td class=\"left\">\n" +
                             "              <h2>"+str(per)+"</h2>\n" +
                             "          </td>\n")
                    per += 1
                while int(element[1]) != pos:
                    form += ("          <td class=\"dummy\"></td>\n")
                    pos += 1
                form += ("          <td class=\""+kind+"\">\n" +
                         "              <h5>"+element[2]+"</h5>\n" +
                         "              <li>"+element[3]+"</h4>\n" +
                         "              <ul>\n" +
                         "                  <li style=\"font-size:20px;\"><h4>"+element[0]+"</h4></li>\n" +
                         "                  <li style=\"font-size:16px;\">"+element[4]+"</li>\n" +
                         "                  <li>"+element[5]+"</li>\n" +
                         "              </ul>\n" +
                         "          </td>\n")
                pos += 1
                if pos == 18:
                    pos = 0
                    form += "       </tr>\n"
            form += ("  </table>\n" +
                     "</body>\n" +
                     "</html>")
            html.write(form)
            html.close()

if __name__ == '__main__':
    periodic_table()
