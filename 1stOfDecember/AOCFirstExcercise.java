import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class AOCFirstExcercise {
		private static final String FILE_PATH = "/Users/nurdanemin/Desktop/input.txt";

		public static void main(String[] args) {
			ArrayList<Integer> calories = new ArrayList<Integer>();
			try {
				getFile(FILE_PATH, calories);
			}catch(FileNotFoundException e) {
				e.getMessage();
			}
			
			Collections.sort(calories);
			
			int x = calories.size();
			int max = calories.get(x-1);   // highest 
			
			int sum =0;
			for (int i=x-3; i<x;  i++) {  // sum of top tree
				sum += calories.get(i);
			}
			System.out.println(max);
			System.out.println(sum);
			
			
		}
		
		public static void getFile(String filePath, ArrayList<Integer> calories) throws FileNotFoundException {
			FileInputStream fis = new FileInputStream(filePath);
			Scanner scan = new Scanner(fis);
			
			int sum =0;
			while(scan.hasNextLine()) {
				
				String Line = scan.nextLine().strip();
				if (Line.isBlank()){
					//System.out.println("hello");
					calories.add(sum);
					sum = 0;
				}else {
					
					sum += Integer.parseInt(Line);
				}
				

				
			}
	}

}
