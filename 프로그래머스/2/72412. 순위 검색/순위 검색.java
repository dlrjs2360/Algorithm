import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(String[] info, String[] query) {
        List<Integer> answer = new ArrayList<>();
        
        HashMap<String, List<Integer>> map = new HashMap<>();
        
        for (String v : info) {
            String[] arr = v.split(" ");
            String key = arr[0] + arr[1] + arr[2] + arr[3];
            List<Integer> vList = map.getOrDefault(key, new ArrayList<>());
            vList.add(Integer.parseInt(arr[4]));
            map.put(key, vList);
        }
        
        // 점수를 미리 정렬 (이진 탐색을 위해)
        for (Map.Entry<String, List<Integer>> entry : map.entrySet()) {
            map.put(entry.getKey(), entry.getValue().stream().sorted().collect(Collectors.toList()));
        }
        
        // 쿼리 처리
        for (String q : query) {
            String[] qArr = q.replace("and", "").replace("  ", " ").split(" ");
            Queue<String> queue = new LinkedList<>();
            queue.add("");
            List<String> tmp = new ArrayList<>();
            
            for (int i = 0; i < 4; i++) {
                tmp.clear();
                while (!queue.isEmpty()) {
                    String s = queue.poll();
                    if (qArr[i].equals("-")) {
                        switch (i) {
                            case 0:
                                tmp.add(s + "cpp");
                                tmp.add(s + "java");
                                tmp.add(s + "python");
                                break;
                            case 1:
                                tmp.add(s + "backend");
                                tmp.add(s + "frontend");  // 오타 수정
                                break;
                            case 2:
                                tmp.add(s + "junior");
                                tmp.add(s + "senior");
                                break;
                            case 3:    
                                tmp.add(s + "chicken");
                                tmp.add(s + "pizza");
                                break;
                        }
                    } else { 
                        tmp.add(s + qArr[i]); 
                    }
                }
                tmp.stream().forEach(queue::add);
            }
            
            int target = Integer.parseInt(qArr[4]);
            int res = 0;
            while (!queue.isEmpty()) {
                String qk = queue.poll();
                if (!map.containsKey(qk)) { 
                    continue; 
                }
                List<Integer> qv = map.get(qk);
                
                // 이진 탐색
                int left = 0;
                int right = qv.size() - 1;
                while (left <= right) {  // 수정된 조건
                    int mid = (left + right) / 2;
                    int val = qv.get(mid);
                    if (val >= target) {  // 수정된 조건
                        right = mid - 1;
                    } else {
                        left = mid + 1;
                    }
                }
                
                res += (qv.size() - left);
            }
            
            answer.add(res);
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}
