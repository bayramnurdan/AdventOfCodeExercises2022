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
			for (int i=0; i<calories.size(); i++) {
				System.out.println(calories.get(i));
			}
			System.out.println(Collections.max(calories));
			 
			
			
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
