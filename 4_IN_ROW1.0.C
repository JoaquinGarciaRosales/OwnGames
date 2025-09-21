#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define ROW 6
#define COLUMN 7

void confirmation();

void printer(char board[ROW][COLUMN]);

int main(){
	char gameboard[ROW][COLUMN];
	for (int i=0; i<ROW;i++){
		for (int j=0; j<COLUMN; j++){
			gameboard[i][j] = '_';
		}
	} 
   printf("\nHello users, decide who starts.\n\nPlayer 1 plays with O.\nPlayer 2 plays with @.\n");
   confirmation();
   bool win=false;
   int turn = 0;

   do {
   	system("cls");
   	printer(gameboard);
   	int playerTurn = (turn % 2) + 1;
   	int selection;
   	printf("Player %d make your move:", playerTurn);
   	scanf("%d", &selection);
   	
   	if (playerTurn==1){
   		for (int i1=0; i1<ROW;i1++){
				if (gameboard[i1+1][selection-1]!='_'){
   				gameboard[i1][selection-1]='O';
   				break;
				}
			}
		}
		else {
			for (int i1=0; i1<ROW;i1++){
				if (gameboard[i1+1][selection-1]!='_'){
   				gameboard[i1][selection-1]='@';
   				break;
				}
			}
		}
		
   	turn ++;
	} while (win == false);

}

void confirmation(){
	char confirm;
	confirm = '0';
	do {
		printf("\nPRESS 1 AND ENTER TO CONTINUE: ");
		scanf("%c", &confirm);
	} while (confirm != '1');
}

void printer(char board[ROW][COLUMN]){
	for (int i=0; i<ROW;i++){
		for (int j=0; j<COLUMN; j++){
			printf("|%c|", board[i][j]);
		}
		printf("\n");
		for (int j1=0; j1<COLUMN; j1++){
			printf("");
		}
	}
}
