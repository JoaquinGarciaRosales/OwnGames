#include <stdio.h>
#include <stdlib.h>
//     O
//    /|\
//    /\     

int is_word(char c);

void clear();

int player1_validator(char *word);

void hangman(int lifes);

int main(){
	
	char *word;
	
	
	word = (char *)malloc(46 * sizeof(char));
	if (word == NULL){
		printf("Unable to alocate word");
		return 1;
	}
	
	//validate entry
	int new_size=player1_validator(word);
	
	word= (char *) realloc(word, (new_size+1) * sizeof(char));
	word[new_size]='\0';
	
	int tried_words_counter=0;
	char *tried_words;
	tried_words = (char *)malloc(1 * sizeof(char));
	tried_words[0]='\0';
	
	int guessed_words_counter=0;
	char *guessed_words;
	guessed_words = (char *)malloc(1 * sizeof(char));
	guessed_words[0]='\0';
	
	int tries = 6;
	
	//maingameloop
	do {
		//-------------------- UI
		clear();
		printf("___________________________________________________________________________\n");
		printf("| Lives remaining %d                                                         |\n", tries);
		printf("___________________________________________________________________________\n\n");
		printf("Used letters:");
		if (*(tried_words)!='\0'){
			int try_printed= 0;
			do {
				printf("  %c  ", *(tried_words+try_printed));
				try_printed++;
			} while(*(tried_words+(try_printed))!='\0');
			printf("\n\n");
		}
		hangman(tries);
		
		int printed_spaces=0;
		for (int i = 0; *(word + i) != '\0'; i++){
			
			int found = 0;

			for (int j=0; *(guessed_words + j) != '\0'; j++){
				if(*(guessed_words + j)==*(word + i)){
					found = 1;
					printf(" %c ", *(word + i));
					break;
				}
			}
			if (found==0 && *(word + i) != '\0'){
				printed_spaces++;
				printf(" _ ");
			}
		}
		printf("\n\n");
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
			printf("Insert a letter to guess (onlylowercase characters): ");
			scanf(" %c", &guess);
			
			//Verificacion de caracter unico
			int c;
			c = getchar();
			
			if (c != '\n'){
				while (c != '\n' && c != EOF) {
	      c = getchar();
	   }
				printf("\nInvalid input (only one character allowed), try again.\n");
			   continue;
			}
			
			//verificación de caracter numérico
			if (is_word(guess)==0){
				valid_letter=0;
				printf("\nInvalid input, try again.\n");
			}
			for (int i=0; *(tried_words+i)!='\0';i++){
				if (*(tried_words+i)==guess){
					valid_letter=0;
					printf("\nAlready tried letter try again.\n");
					break;
				}
			}
			for (int i=0; *(guessed_words+i)!='\0';i++){
				if (*(guessed_words+i)==guess){
					valid_letter=0;
					printf("\nAlready tried letter try again.\n");
					break;
				}
			}
			if (valid_letter==1){
				break;
			}
		} while (1);
		
		
		printf("Used letter %c\n", guess);
		
		tried_words[tried_words_counter] = guess;
		tried_words_counter++;
		tried_words= (char *) realloc(tried_words, (tried_words_counter+1) * sizeof(char));
		tried_words[tried_words_counter]='\0';
		
		int success = 0;
		for (int i=0; *(word+i)!='\0'; i++){
			if (guess == *(word+i)){
				guessed_words[guessed_words_counter] = guess;
				guessed_words_counter++;
				guessed_words= (char *) realloc(guessed_words, (guessed_words_counter+1) * sizeof(char));
				guessed_words[guessed_words_counter]='\0';
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
		printf("You lose the secret word was: %s", word);
	}
	
	free(word);
	free(guessed_words);
	free(tried_words);
	
	return 0;
}

int player1_validator(char *word){
	int letters_counter = 0;
	int validator = 0;

	do {
		validator = 1;
		printf("Insert the secret word with only lowercase characters and maximum of 45 caracters (further ones won't be taken into account): ");
		scanf("%45s", word);
		
		for (int i = 0; *(word + i) != '\0'; i++){
			if (is_word(*(word+i))==0){
				validator = 0;
				printf("Invalid entry, please try again.\n");
				break;
			}
		}
	} while (validator == 0);
	
	for (int i = 0; *(word+i)!='\0'; i++){
		if (is_word(*(word+i))==1){
			letters_counter ++;
		}
	}
	
	clear();
	return letters_counter;
}

void hangman(int lives){
	switch(lives){
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
