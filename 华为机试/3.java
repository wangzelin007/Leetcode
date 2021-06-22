public int minInterviewers(int[][] intervals) {
      if(intervals==null||intervals.length==0) {
          return 0;
      }
      PriorityQueue<Integer> pq = new PriorityQueue<>();
      Arrays.sort(intervals, Comparator.comparingInt(i -> i[0]));
      pq.add(intervals[0][1]);
      for(int i=1;i!=intervals.length;i++) {
          int last=pq.peek();
          if(last<=intervals[i][0]) {
              pq.poll();
              pq.add(intervals[i][1]);
          }else{
              pq.add(intervals[i][1]);
          }
      }
      return pq.size();
  }