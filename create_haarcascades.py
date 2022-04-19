import os
import shutil

def CascadeOneImage(PastaPrincipal):
    PositivasCriada = False
    VetorPositivasCriado = False
    ClassificadorCriado = False

    ListaElementos = os.listdir(PastaPrincipal)
    print(os.listdir(PastaPrincipal))

    for ElementosLista in ListaElementos:
        if ElementosLista == 'positivas':
            PositivasCriada = True

        if ElementosLista == 'positivas.vec':
            VetorPositivasCriado = True

    if PositivasCriada == False:
        print(os.system('opencv_createsamples -img 1.jpg -bg negativas/bg.txt -info positivas/positivas.lst -maxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1800 -bgcolor 255 -bgtresh 8'))

    if VetorPositivasCriado == False:
        print(os.system('opencv_createsamples -info positivas/positivas.lst -num 1800 -w 18 -h 18 -vec positivas.vec'))

    PastaNegativas = os.path.join(PastaPrincipal, 'negativas')
    CaminhoPastaNegativas = PastaNegativas

    for ElementosPastaNegativas in os.listdir(CaminhoPastaNegativas):
        if ElementosPastaNegativas == 'classificador':
            CaminhoPastaClassificador = os.path.join(PastaNegativas, 'classificador')

            if os.listdir(CaminhoPastaClassificador) == []:
                print('pasta vazia')
                ClassificadorCriado = False

            else:
                for ElementosPastaClassificador in os.listdir(CaminhoPastaClassificador):
                    if ElementosPastaClassificador == 'cascade.xml':
                        ClassificadorCriado = True
                        print("classificador criado")

    if ClassificadorCriado == False:
    
        print("------------------ Movendo arquivos necessários para a pasta negativas --------------------")

        Caminho1 = PastaPrincipal
        Caminho2 = CaminhoPastaNegativas

        print(Caminho1, "\n ", Caminho2)

        ListaArquivosPasta = os.listdir(Caminho1)

        for ArquivosPasta in ListaArquivosPasta:
            print(ArquivosPasta)
            if ArquivosPasta == 'opencv_traincascade.exe':
                try:
                    shutil.copy('opencv_traincascade.exe', Caminho2)
                    print('Arquivo copiado com sucesso!')
                except:
                    print('Erro')
    
            if ArquivosPasta == 'opencv_world400.dll':
                try:
                    shutil.copy('opencv_world400.dll', Caminho2)
                    print('Arquivo copiado com sucesso!')
                except:
                    print('Erro')
    
            if ArquivosPasta == 'positivas.vec':
                try:
                    shutil.copy('positivas.vec', Caminho2)
                    print('Arquivo copiado com sucesso!')
                except:
                    print('Erro')

        print("------------------ Criação da pasta classificadores --------------------")

        try:
            CriarPastaClassificadores = os.path.join(PastaNegativas, 'classificador')
            os.makedirs(CriarPastaClassificadores)
            print('Pasta classificadores criada')
        except:
            print('Erro ao criar pasta classificadores')

        print("------------------ Treinamento do haarcascade --------------------")
        # try:
        #     print(os.getcwd())
        #     os.chdir(CaminhoPastaNegativas)
        #     print(os.getcwd())
        #     os.system('opencv_traincascade -data classificador -vec positivas.vec -bg bg.txt -numPos 1600 -numNeg 800 -numStages 10 -w 18 -h 18 -precalcBufSize 1024 -precalcIdzBufSize 1024')
        #     print("Haarcascade criado")

        # except:
        #     print("Erro ao criar classificador")

    else:
        print("Classificador já criado")

def CascadeMultipleImages(CaminhoPastaImagens, PastaPrincipal):
    PositivasCriada = False;
    VetorFinal = False;
    VetoresPositivas = False;
    ClassificadorCriado2 = False;

    ListaArquivosPastaPrincipal = os.listdir(PastaPrincipal)
    
    for ListaElement in ListaArquivosPastaPrincipal:
        if ListaElement == 'vetor_final.vec':
            VetorFinal = True

    PastaNegativas = os.path.join(PastaPrincipal, 'negativas')
    CaminhoPastaNegativas = PastaNegativas

    for ElementosPastaNegativas in os.listdir(CaminhoPastaNegativas):
        if ElementosPastaNegativas == 'classificador':
            CaminhoPastaClassificador = os.path.join(PastaNegativas, 'classificador')

            if os.listdir(CaminhoPastaClassificador) == []:
                print('pasta vazia')
                ClassificadorCriado2 = False

            else:
                for ElementosPastaClassificador in os.listdir(CaminhoPastaClassificador):
                    if ElementosPastaClassificador == 'cascade.xml':
                        ClassificadorCriado2 = True
                        print("classificador criado")


    NumImagensPositivas = len(os.listdir(CaminhoPastaImagens))
    print(NumImagensPositivas)
    ArquivosImagens = os.listdir(CaminhoPastaImagens)

    for numVec in range(NumImagensPositivas - 1):
        CriarVetor = ArquivosImagens[numVec]
        CaminhoImagem = os.path.join(CaminhoPastaImagens, CriarVetor)
        print(CaminhoImagem)
        shutil.copy(CaminhoImagem, PastaPrincipal)
        for ElementosPastaPrincipal in ListaArquivosPastaPrincipal:
            if ElementosPastaPrincipal == 'positivas{0}'.format(numVec):
                PastaPositivasCriada = True
        
        if PastaPositivasCriada == False:
            print(os.system('opencv_createsamples -img {0} -bg negativas/bg.txt -info positivas{1}/positivas{2}.lst -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -w 48 -h 48 -num 300 -bgcolor 255 -bgtresh 8'.format(CriarVetor, numVec, numVec)))
            print(os.system('opencv_createsamples -info positivas{0}/positivas{1}.lst -num 2000 -w 20 -h 20 -vec vetor{2}.vec'.format(numVec, numVec, numVec)))

        else:
            print("Vetor {0} criado e pasta {0} criada".format(numVec))

    ListaArquivosPastaPrincipal = os.listdir(PastaPrincipal)

    PastaVec = os.path.join(PastaPrincipal, 'vec')

    for NumArquivoVec in range(NumImagensPositivas - 1):
        for ArquivosVec in ListaArquivosPastaPrincipal:
            if ArquivosVec == 'vetor{0}.vec'.format(NumArquivoVec):
                shutil.move(ArquivosVec, PastaVec)

    print(os.system('python mergevec.py -v vec/ -o vetor_final.vec'))
    
    if ClassificadorCriado2 == False:
    
        print("------------------ Movendo arquivos necessários para a pasta negativas --------------------")

        Caminho1 = PastaPrincipal
        Caminho2 = CaminhoPastaNegativas

        print(Caminho1, "\n ", Caminho2)

        ListaArquivosPasta = os.listdir(Caminho1)

        for ArquivosPasta in ListaArquivosPasta:
            print(ArquivosPasta)
            if ArquivosPasta == 'opencv_traincascade.exe':
                try:
                    shutil.copy('opencv_traincascade.exe', Caminho2)
                    print('Arquivo copiado com sucesso!')
                except:
                    print('Erro')
    
            if ArquivosPasta == 'opencv_world400.dll':
                try:
                    shutil.copy('opencv_world400.dll', Caminho2)
                    print('Arquivo copiado com sucesso!')
                except:
                    print('Erro')
    
            if ArquivosPasta == 'vetor_final.vec':
                try:
                    shutil.copy('vetor_final.vec', Caminho2)
                    print('Arquivo copiado com sucesso!')
                except:
                    print('Erro')

        print("------------------ Criação da pasta classificadores --------------------")

        try:
            CriarPastaClassificadores = os.path.join(PastaNegativas, 'classificador')
            os.makedirs(CriarPastaClassificadores)
            print('Pasta classificadores criada')
        except:
            print('Erro ao criar pasta classificadores')

        print("------------------ Treinamento do haarcascade --------------------")
        try:
            print(os.getcwd())
            os.chdir(CaminhoPastaNegativas)
            print(os.getcwd())
            os.system('opencv_traincascade -data classificador -vec vetor_final.vec -bg bg.txt -numPos 1800 -numNeg 800 -numStages 10 -w 20 -h 20 -precalcValBufSize 1024 -precalcIdxBufSize 1024')
            print("Haarcascade criado")

        except:
            print("Erro ao criar classificador")

    else:
        print("Classificador já criado")


PastaPrincipal = os.getcwd()

CaminhoPastaImagens = os.path.join(PastaPrincipal, 'imagens')

if len(os.listdir(CaminhoPastaImagens)) == 1:
    CascadeOneImage(PastaPrincipal)

elif len(os.listdir(CaminhoPastaImagens)) > 1:
    CascadeMultipleImages(CaminhoPastaImagens, PastaPrincipal)

print("Concluído!")