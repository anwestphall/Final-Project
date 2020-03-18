"""Ask for vegetables print calendar to PDF."""
import PyPDF2
import fpdf
from fpdf import FPDF


def pdf_setup(d_list):
    
    pdf = FPDF()
    pdf.add_page()
    font = input("pick a font (Arial, courier, times): ")
    font_size = int(input("pick a font size(1-20): "))
    text_color1 = input("pick a color(red, green, blue): ")
    text_color2 = input("pick a color(red, green, blue): ")
    if text_color1 == "red":
        pdf.set_text_color(255,0,0)
    if text_color1 == "green":
        pdf.set_text_color(0,200,55)
    if text_color1 == "blue":
        pdf.set_text_color(0,0,255)
    pdf.set_font(f"{font}", size= font_size)
    pdf.cell(200, 10, txt = "Planting Calendar!", ln= 1, align="C")
    pdf.cell(200, 10, txt = "  ", ln= 1, align="C")
    pdf.cell(200, 10, txt = "Plant | Date to plant", ln = 1, align = "C")
    pdf.cell(200, 10, txt = "  ", ln= 1, align="C")
    counter = 0
    for i in d_list:
        i = str(i)
        i = i.replace("'", "").replace("]", "").replace("[", "")
        i = i.replace("mar", "March").replace("apr", "April").replace("may", "May").replace("feb", "Februrary")
        i = i.replace(" ", "\t")
        if counter %2 == 0:
            if text_color2 == "red":
                pdf.set_text_color(255,0,0)
            if text_color2 == "green":
                pdf.set_text_color(0,200,55)
            if text_color2 == "blue":
                pdf.set_text_color(0,0,255)
        if counter %2 != 0:
            if text_color1 == "red":
                pdf.set_text_color(255,0,0)
            if text_color1 == "green":
                pdf.set_text_color(0,200,55)
            if text_color1 == "blue":
                pdf.set_text_color(0,0,255)
        pdf.cell(200, 10, txt= f"{i}", ln=20, align= "C")
        counter += 1
        print(i)

    pdf.output("Planting_calendar.pdf")


def get_veges(str3):
    desired_list = []
    print("Pick your vegetables(beans, beets, bell peppers,\
 broccoli, brussels sprouts, cabbage, cantaloupes, carrots,\
 cauliflower, celery, corn, cucumbers, eggplants, lettuce, okra,\
 onions, parnsnips, peas, potatoes, pumpkins, radishes, spinach,\
 zucchini, sweet potatoes, swiss chard, tomatoes, turnips,\
 watermelons) ")
    while True:
        wanted_veges = input("(type 'quit' to stop): ")
        if wanted_veges == "quit":
            print("you are done listing vegetables")
            break
        for i in str3:
            if wanted_veges in i:
                desired_list.append(i)
    return desired_list



def main():
  with open("calendar.txt", "r") as fin:
    list_1 = []
    for line in fin:
        list_1.append(line)
    string_1 = str(list_1)
    string_2 = string_1.replace('\\t', " ").replace('\\n', "").replace("]", "").replace("'", "").replace("[", "")
    string_3 = string_2.split(",")
    d_list = get_veges(string_3)
    pdf_setup(d_list)






    




if __name__ == "__main__":
    main()