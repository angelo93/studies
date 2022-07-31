//***************************************************************
//
//  Developer:     Michael Navarro
//
//  Project #:     Six
//
//  File Name:     Project6.java
//
//  Course:        COSC 3365 – Distributed Databases Using Hadoop 
//
//  Due Date:      3-26-2022
//
//  Instructor:    Prof. Fred Kumi 
//
//  Description:   Calculates the 
//                 appears in a document
//
//***************************************************************

import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class Project6Driver
{
	//***************************************************************
    //
    //  Method:       main
    // 
    //  Description:  The main method of the program
    //
    //  Parameters:   String array
    //
    //  Returns:      Output file with city location and success rate
    //
    //**************************************************************
	public static void main(String[] args) // throws Exception
	{
		if (args.length != 2)
		{
			System.err.println("Usage: WordCount <input path> <output path>");
			System.exit(-1);
		}
		
		// The Driver class instantiates a Job object. The Job object creates
		// and stores the configuration options for the Job, including the
		// classes to be used as the Mapper, Reducer, and Combiner, input and output
		// directories, and other options, such as the Job name that will
		// display in the YARN ResourceManager UI.
		Configuration conf = new Configuration();
		
		String[] files;
		try {
			files = new GenericOptionsParser(conf, args).getRemainingArgs();
			
			// Get input and output locations
			Path input = new Path(files[0]);
			Path output = new Path(files[1]);

			// Job name that will be displayed in the YARN ResourceManager UI.
			Job job = Job.getInstance(conf, "wordcount");

			// Set input and output locations
			FileInputFormat.addInputPath(job, input);
			FileOutputFormat.setOutputPath(job, output);

			// The Driver class
			job.setJarByClass(Project6Driver.class);
			
			//Set Input and Output formats
			job.setInputFormatClass(TextInputFormat.class);
			job.setOutputFormatClass(TextOutputFormat.class);
			
			//Set Mapper, Reduce, and Combiner classes
			job.setMapperClass(Project6Mapper.class);
			job.setReducerClass(Project6Reducer.class);
			
			//Output types
			job.setOutputKeyClass(Text.class);
			job.setOutputValueClass(Text.class);

			// Submit Job
			 boolean status = job.waitForCompletion(true);
			 if (status)
			    System.exit(0);
			 else
			    System.exit(1);
			 // end if
			 
		} catch (IOException e) {
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
