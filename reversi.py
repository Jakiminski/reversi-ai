#!/usr/bin/env python3
# coding: utf-8

# Reversi / Othello
from reversiboard import *

if __name__ == '__main__':

	print('Welcome to Reversi!')
	while True:
		# Reseta o jogo e o tabuleiro
		mainBoard = getNewBoard()
		resetBoard(mainBoard)
		playerTile, computerTile = enterPlayerTile()
		showHints = False
		turn = whoGoesFirst()
		print('O ' + turn + ' começa o jogo.')
		while True:
			if turn == 'player':
				# Player's turn.
				if showHints:
					validMovesBoard = getBoardWithValidMoves(mainBoard, playerTile)
					drawBoard(validMovesBoard)
				else:
					drawBoard(mainBoard)
				showPoints(playerTile, computerTile, mainBoard)
				move = getPlayerMove(mainBoard, playerTile)
				if move == 'quit':
					print('Obrigado por jogar!')
					sys.exit() # terminate the program
				elif move == 'hints':
					showHints = not showHints
					continue
				else:
					makeMove(mainBoard, playerTile, move[0], move[1])
				if getValidMoves(mainBoard, computerTile) == []:
					break
				else:
					turn = 'computer'
			else:
				# Computer's turn.
				drawBoard(mainBoard)
				showPoints(playerTile, computerTile, mainBoard)
				input('Pressione \'Enter\' para ver a jogada do computador.')
				x, y = getComputerMove(mainBoard, computerTile)
				makeMove(mainBoard, computerTile, x, y)
				if getValidMoves(mainBoard, playerTile) == []:
					break
				else:
					turn = 'player'
		# Mostra o resultado final.
		drawBoard(mainBoard)
		scores = getScoreOfBoard(mainBoard)
		print('X: %s ponto(s) \nO: %s ponto(s).' % (scores['X'], scores['O']))
		if scores[playerTile] > scores[computerTile]:
			print('Você venceu o computador por %s ponto(s)! \nParabéns!' % (scores[playerTile] - scores[computerTile]))
		elif scores[playerTile] < scores[computerTile]:
			print('Você perdeu!\nO computador venceu você por %s ponto(s).' % (scores[computerTile] - scores[playerTile]))
		else:
			print('Empate!')
		if not playAgain():
			break