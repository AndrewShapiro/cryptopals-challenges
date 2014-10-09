#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int hexToBase64(char* hex, char * output);
char intToCharBase64(int num);
int hexStringtoHex(char* in, char* out);

int main (){
	char* hexString  = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
	char* parsedString = calloc(strlen(hexString)/2 + 1, sizeof(char));
	hexStringtoHex(hexString, parsedString);
	int paddingSigns = strlen(parsedString) % 3 ? 4 : 0;
	char* output = malloc(strlen(parsedString) * 4 /3  + paddingSigns + 1);

	hexToBase64(parsedString, output);
	printf("%s\n", output);
	free(output);
	return 0;
}

int hexStringtoHex(char* in, char* out){
	int i, j=0;
	char temp[3] = {0};
	for(i=0; i< strlen(in)/2 ; i++){	
		temp[0] = in[j];
		temp[1] = in[j+1];
		j += 2;
		out[i] = strtol(temp, NULL, 16);
	}
	return 0;
}

int hexToBase64(char* hex, char * output) {
	int hexLen = strlen(hex);
	int loopLen = hexLen/3;
	int i, j = 0;

	for(i = 0; i< loopLen; i++){
		char a = (hex[i*3] & 0b11111100 )>> 2;
		char b = (hex[i*3] & 0b00000011) << 4 | (hex[i*3 + 1] & 0b11110000) >> 4;
		char c = (hex[i*3 + 1] & 0b00001111) << 2 | (hex[i*3 + 2] & 0b11000000) >> 6;
		char d = (hex[i*3 + 2] & 0b00111111);

		output[j++] = intToCharBase64(a);
		output[j++] = intToCharBase64(b);
		output[j++] = intToCharBase64(c);
		output[j++] = intToCharBase64(d);
	}
	
	int numEndBytes = hexLen % 3;
	if (numEndBytes == 1){
		char a = (hex[i*3] & 0b11111100 )>> 2;
		char b = (hex[i*3] & 0b00000011) << 4;
		output[j++] = intToCharBase64(a);
		output[j++] = intToCharBase64(b);
		output[j++] = '=';
		output[j++] = '=';
	}else if(numEndBytes == 2){
		char a = (hex[i*3] & 0b11111100 )>> 2;
		char b = (hex[i*3] & 0b00000011) << 4 | (hex[i*3 + 1] & 0b11110000) >> 4;
		char c = (hex[i*3 + 1] & 0b00001111) << 2;

		output[j++] = intToCharBase64(a);
		output[j++] = intToCharBase64(b);
		output[j++] = intToCharBase64(c);
		output[j++] = '=';
	}
	output[j++] = 0;
	return 0;
}

char intToCharBase64(int num){
	if(num >= 0 && num <= 25){
		return (char) (num +  'A');
	}else if(num >= 26 && num <= 51){
		return (char) (num - 26 + 'a'); //ALSO KNOWN AS 71
	}else if(num >= 52 && num <= 61){
		return (char) (num - 52 + '0');
	}else if(num == 62){
		return '+';
	}else if(num == 63){
		return '/';
	}
	return (char) -1;
}