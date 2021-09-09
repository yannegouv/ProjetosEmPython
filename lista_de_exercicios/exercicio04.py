print('valos calcular a  nota final e avaliar se o aluno deve passar de ano, para isso insira as 4 notas referentes aos bimestres')

notaUm = int(input('Primeira nota: '))
notaDois = int(input('Segunda nota: '))
notaTres = int(input('Terceira nota: '))
notaQuatro = int(input('Quarta nota: '))

notaFinal = ((notaUm + notaDois + notaTres + notaQuatro) /4 ) 

print ('A nota final alcançada pelo aluno é de: ' , notaFinal , 'pontos')