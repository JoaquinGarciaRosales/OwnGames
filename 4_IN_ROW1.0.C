#include <stdio.h>
#include <stdlib.h>

#define ROW 6
#define COLUMN 7

int getInt();

void confirmation();

void clear();

void printer(char board[ROW][COLUMN]);

void gameLoop(char board[ROW][COLUMN]);

int validator(char board[ROW][COLUMN], int turn);

int main(){
	char gameboard[ROW][COLUMN];
	for (int i=0; i<ROW;i++){
		for (int j=0; j<COLUMN; j++){
			gameboard[i][j] = '_';
		}
	} 
	gameLoop(gameboard);
}

void confirmation(){
	int confirm = 0;
	do {
		printf("\nPRESS 1 AND ENTER TO CONTINUE: ");
		confirm = getInt();
	} while (confirm != 1);
}

void printer(char board[ROW][COLUMN]){
	for (int i = 0; i < ROW; i++){
		for (int j = 0; j < COLUMN; j++){
			printf("|%c|", board[i][j]);
		}
		printf("\n");
	}
}

void gameLoop(char board[ROW][COLUMN]){
	printf("\nHello users, decide who starts.\n\nPlayer 1 plays with O.\nPlayer 2 plays with @.\n\nRules: The player who gets 4 chips in line wins the game (lines could be horizontal, vertical and diagonal)\n");
   confirmation();
	int win=0;
   int turn = 0;
	do {
   	clear();
   	printer(board);
   	int selection;
   	
   	do{
   		printf("Player %d make your move(select a number between 1 and 7):", ((turn % 2) + 1));
   		selection = getInt();
		} while(board[0][selection-1] != '_' || selection < 1 || selection > 7);
   	
   	
   	if (((turn % 2) + 1)==1){
   		for (int i = 0; i < ROW ; i++){
				if (board[i+1][selection-1]!='_'){
   				board[i][selection-1]='O';
   				break;
				}
			}
		}
		else {
			for (int i = 0; i < ROW ; i++){
				if (board[i+1][selection-1]!='_'){
   				board[i][selection-1]='@';
   				break;
				}
			}
		}
		
   	turn ++;
   	if (turn>6){
   		win = validator(board,turn);
		}
		
	} while (win == 0);
	
	clear();
   printer(board);
   printf("\nPlayer %d wins at turn %d.\n", ((turn % 2) + 1), turn);
}

int validator(char board[ROW][COLUMN],int turn){
	
	//Horizontales
	for (int i = 0; i < ROW; i++){
		int counter = 1;
		for (int j = 0; j < COLUMN-1; j++){
			if (board[i][j] != '_' && board[i][j]==board[i][j+1]){
				counter ++;
				if (counter == 4){
					return 1;
				}
			}
			else {
				counter = 1;
			}
		}
	}
	
	//Verticales
	for (int j = 0; j < ROW-1; j++){
		int counter = 1;
		for (int i = 0; i < COLUMN; i++){
			if (board[i][j] != '_' && board[i][j]==board[i+1][j]){
				counter ++;
				if (counter == 4){
					return 1;
				}
			}
			else{
				counter = 1;
			}
		}
	}
	
	if (turn>9){
		//Diagonales hacia abajo derecha
		for (int i = 0; i < ROW - 3; i++) {
	      for (int j = 0; j < COLUMN - 3; j++) {
	         int counter = 1;
	         int i1 = i;
	         int j1 = j;
	         while (i1 < ROW - 1 && i1 < COLUMN - 1) {
	            if (board[i1][j1] != '_' && board[i1][j1] == board[i1+1][j1+1]) {
	               counter++;
	               if (counter == 4) {
	                  return 1;
	               }
	         	} else {
	               counter = 1;
	            }
	            i1++;
	            j1++;
	      	}
			}
		}
		
		//Diagonales hacia abajo izquierda
		for (int i = 0; i < ROW - 3; i++) {
	      for (int j = 3; j < COLUMN; j++) {
	         int counter = 1;
	         int i1 = i;
	         int j1 = j;
	         while (i1 < ROW - 1 && j1 > 0) {
	            if (board[i1][j1] != '_' && board[i1][j1] == board[i1+1][j1-1]) {
	               counter++;
	               if (counter == 4) {
	                  return 1;
	               }
	         	} else {
	               counter = 1;
	            }
	            i1++;
	            j1--;
	      	}
			}
		}
	}
	
	return 0;
}
// Instruccoines especiales
void clear() {
	#ifdef _WIN32
   	system("cls");
	#else
   	system("clear");
	#endif
}

int getInt(){
	int entry;
	char c;
   int num;

   while (1) {
      entry = scanf("%d%c", &num, &c);
      if (entry == 2 && c == '\n') {
         return num;
      } 
		else {
			printf("Invalid num, try again: ");
         while ((c = getchar()) != '\n' && c != EOF);
      }
   }
}
