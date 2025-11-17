#include <stdio.h>
#include <stdlib.h>
//     O
//    /|\
//    /\     

int is_word(char c);

void clear();

void player1_validator(char *word);

void hangman(int lifes);

int main(){
	
	char *word;
	
	
	word = (char *)malloc(46 * sizeof(char));
	if (word == NULL){
		printf("Unable to alocate word");
		return 1;
	}
	
	//validate entry
	player1_validator(word);
	
	//*pendiente función para redimensionar word
	
	int tried_words_counter=1;
	char *tried_words;
	tried_words = (char *)malloc(1 * sizeof(char));
	
	int guessed_words_counter=1;
	char *guessed_words;
	guessed_words = (char *)malloc(1 * sizeof(char));
	
	int tries = 6;
	
	//maingameloop
	do {
		//-------------------- UI
		clear();
		printf("___________________________________________________________________________\n");
		printf("| Lifes remain %d                                                         |\n", tries);
		printf("___________________________________________________________________________\n\n");
		hangman(tries);
		int printed_spaces=0;
		for (int i = 0; *(word + i) != '\0'; i++){
			
			int found = 0;

			for (int j=0; *(guessed_words + j) != '\0'; j++){
				if(*(guessed_words + j)==*(word + i)){
					found = 1;
					printf("%c", *(word + i));
					break;
				}
			}
			if (found==0 && *(word + i) != '\0'){
				printed_spaces++;
				printf("_");
			}
		}
		printf("\n");
		//-------------------- UI
		
		// verify victory
		if(printed_spaces==0){
			printf("\nYou have won\n");
			printf("\nPRESS ENTER TO CONTINUE\n");
			int c2;
			while ((c2 = getchar()) != '\n' && c2 != EOF);
			break;
		}
		
		char guess;
		
		do {
			int valid_letter=1;
			printf("Insert a letter to guess: ");
			scanf(" %c", &guess);
		// *pendiente hacer que solo se acepte 1 caracter	
			//generar una espera
			int c;
			while ((c = getchar()) != '\n' && c != EOF);
			
			for (int i=0; *(tried_words+i)!='\0';i++){
				if (*(tried_words+i)==guess){
					valid_letter=0;
					printf("\nAlready tried letter try again\n");
					break;
				}
			}
			if (valid_letter==1){
				break;
			}
		} while (1);
		
		
		printf("Used leter %c\n", guess);
		
		tried_words[tried_words_counter - 1] = guess;
		tried_words_counter++;
		tried_words= (char *) realloc(tried_words, tried_words_counter * sizeof(char));
		
		
		int success = 0;
		for (int i=0; *(word+i)!='\0'; i++){
			if (guess == *(word+i)){
				guessed_words[guessed_words_counter - 1] = guess;
				guessed_words_counter++;
				guessed_words= (char *) realloc(guessed_words, guessed_words_counter * sizeof(char));
				success = 1;
				printf("You guessed a letter.\n");
				break;
			}
		}
		if (success==0) {
			tries--;
			printf("You failed the letter.\n");
		}	
				
		
		printf("PRESS ENTER TO CONTINUE");
		int c1;
		while ((c1 = getchar()) != '\n' && c1 != EOF);
		
	} while (tries > 0); 
	
	clear();
	
	if (tries == 0){
		hangman(tries);
		printf("You loose.");
	}
	
	free(word);
	free(guessed_words);
	free(tried_words);
	
	return 0;
}

void player1_validator(char *word){
	int validator = 0;
	do {
		validator = 1;
		printf("Insert the secret word (only lowercase caracters): ");
		scanf("%s", word);
			//*pendiente función para no admitir mas de 45 caracteres
			
		for (int i = 0; *(word + i) != '\0'; i++){
			if (is_word(*(word+i))==0){
				validator = 0;
				printf("Unvalid entry, please try again.\n");
				break;
			}
		}
	} while (validator == 0);
	clear();
}

void hangman(int lifes){
	switch(lifes){
		case 6:
			printf(" |\n\n");
			break;
		case 5:
			printf(" |\n O\n\n");
			break;
		case 4:
			printf(" |\n O \n/\n\n");
			break;
		case 3:
			printf(" |\n O \n/|\n\n");
			break;
		case 2:
			printf(" |\n O \n/|\\\n\n");
			break;
		case 1:
			printf(" |\n O \n/|\\\n/\n\n");
			break;
			
		case 0:
			printf(" |\n O \n/|\\\n/ \\\n\n");
			break;
	}
}

int is_word(char c) {
	if (c >= 'a' && c <= 'z'){
		return 1;
	}
	else {
		return 0;
	}
}

void clear() {
	#ifdef _WIN32
   	system("cls");
	#else
   	system("clear");
	#endif
}
