
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

class Main {

	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream(System.getProperty("user.dir") + "/input.txt"));

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int t = Integer.parseInt(br.readLine());

		List<Integer> answer = new ArrayList<>();
		for (int i = 123; i <= 987; i++) {
			answer.add(i);
		}

		int s, b, ts, tb;
		String[] num;
		for (int i = 0; i < t; i++) {
			List<String> arr = Arrays
				.stream(br.readLine().split(" "))
				.collect(Collectors.toList());

			num = arr.get(0).split("");
			s = Integer.parseInt(arr.get(1));
			b = Integer.parseInt(arr.get(2));

			List<Integer> list = new ArrayList<>();

			for (int j = 123; j <= 987; j++) {
				ts = 0;
				tb = 0;
				String[] numj = String.valueOf(j).split("");
				if (Arrays.asList(numj).contains("0")) {
					continue;
				}
				if (numj[0].equals(numj[1]) || numj[1].equals(numj[2]) || numj[0].equals(numj[2])) {
					continue;
				}
				for (int k = 0; k < 3; k++) {
					if (numj[k].equals(num[k])) {
						ts++;
					} else if (Arrays.asList(num).contains(numj[k])) {
						tb++;
					}
				}

				if (ts == s && tb == b) {
					list.add(j);
				}
			}

			answer = answer.stream().filter(list::contains).collect(Collectors.toList());
		}

		bw.write(String.valueOf(answer.size()));
		bw.flush();
    }
}
