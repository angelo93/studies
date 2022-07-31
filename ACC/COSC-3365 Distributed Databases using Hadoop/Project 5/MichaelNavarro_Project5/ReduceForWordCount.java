import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

//***************************************************************
//
//  Class:        ReducerForWordCount
//
//  Method:       reduce
// 
//  Description:  This is the Reducer Class program for the
//                WordCount program using MapReduce
//
//  Parameters:   Method parameters: Test, Iterable<IntWritable>, and Context
//
//  Returns:      NAME SUM(values) 
//
//**************************************************************
public class ReduceForWordCount extends Reducer<Text, IntWritable, Text, IntWritable>
{
	@Override
	public void reduce(Text word, Iterable<IntWritable> values, Context context)
			throws IOException, InterruptedException
	{   
		// An object Implementing Iterable allows it to be iterated
	    // An iterable interface allows an object to be the target of
		// enhanced for loop(for-each loop). 
	    // Key=JOHN, Value=[1,1,1,1,1,1,...,1]
	
		int sum = 0;
		for (IntWritable value : values)
		{
			sum += value.get();
		}
		context.write(word, new IntWritable(sum));
	}
}
