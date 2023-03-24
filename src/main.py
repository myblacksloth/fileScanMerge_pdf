
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfReader, PdfFileWriter
import argparse # per gli argomenti della command line

def main():

    parser = argparse.ArgumentParser() # parser degli argomenti della riga di comando

    # aggiungi argomenti al parser
    parser.add_argument('-fa', type=str, help="file A", required=True)
    parser.add_argument('-fb', type=str, help="file B", required=True)
    parser.add_argument('-out', type=str, help="output file", required=True)
    parser.add_argument('-t', type=str, help="titolo del file")
    parser.add_argument('-a', type=str, help="autore del file")

    # ricevi argomenti
    args = parser.parse_args()

    # --------------------------------------------------------------------------------

    source_file_1 = args.fa
    source_file_2 = args.fb

    pdf_path_1 = (
        # Path.home()
            Path().absolute()
            / ""
            / ""
            # / "doc1.pdf" # pdf name
            / source_file_1  # pdf name
    )

    pdf_path_2 = (
        # Path.home()
            Path().absolute()
            / ""
            / ""
            # / "doc1.pdf" # pdf name
            / source_file_2  # pdf name
    )


    # --------------------------------------------------------------------------------

    # ottieni i file pdf
    # i file pdf rispettano le specifiche indicate in ref/1.1
    input_pdf_1 = PdfFileReader(str(pdf_path_1))
    # input_pdf_1 = PdfReader(str(pdf_path_1))
    input_pdf_2 = PdfFileReader(str(pdf_path_2))
    # input_pdf_2 = PdfReader(str(pdf_path_2))

    # --------------------------------------------------------------------------------

    # calcola il nuemro di pagine dei file pdf
    pdf_1_pages = input_pdf_1.getNumPages()
    pdf_2_pages = input_pdf_2.getNumPages()

    # --------------------------------------------------------------------------------
    # indici per prelevare le pagine
    # dal pdf a leggo le pgine dalla prima all'ultima : indice i1
    # dal pdf b leggo le pagine dall'ultima alla prima : indice i2
    # ref/1.2
    i1 = 0
    i2= pdf_2_pages - 1

    # --------------------------------------------------------------------------------

    # crea file pdf di output
    pdf_writer = PdfFileWriter()

    # --------------------------------------------------------------------------------

    # il pdf finale dovra' contenere il massimo numero di pagine dal file con piu' pagine

    for i in range(0, max(pdf_1_pages, pdf_2_pages)):

        if i1 <= pdf_1_pages: # se vi sono pagine da leggere nel pdf 1
            page_1 = input_pdf_1.getPage(i1) # leggi la pagina corrente
            pdf_writer.addPage(page_1) # aggiungi la pagina al pdf di destinazione
            i1 += 1 # incrementa indice per il primo pdf

        if i2 >= 0: # se vi sono pagine da leggere nel pdf 2
            page_2 = input_pdf_2.getPage(i2) # leggi la pagina corrente
            pdf_writer.addPage(page_2) # aggiungi pagina al pdf
            i2 -= 1 # decrementa indice per il secondo pdf

    # --------------------------------------------------------------------------------

    # aggiunta di eventuali metadata al file di output

    # aggiunta del titolo
    if args.t:
        pdf_writer.addMetadata({
            '/Author': args.t
        })

    # aggiunta dell'autore
    if args.a:
        pdf_writer.addMetadata({
            '/Title': args.a
        })

    # --------------------------------------------------------------------------------

    # scrittura del file di output

    output_file = args.out

    pdf_writer.write(output_file)

    # --------------------------------------------------------------------------------



    return 0



if __name__ == '__main__':
    main()