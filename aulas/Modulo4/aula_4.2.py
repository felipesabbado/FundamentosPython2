""" 4.2 Section 2 – Files (file streams, file processing, diagnosing stream problems) """
"""
4.2.11 SECTION SUMMARY

1. A file needs to be open before it can be processed by a program, and it should be closed when the processing is finished.

Opening the file associates it with the stream, which is an abstract representation of the physical data stored on the media. The way in which the stream is processed is called open mode. Three open modes exist:

    read mode – only read operations are allowed;
    write mode – only write operations are allowed;
    update mode – both writes and reads are allowed.

2. Depending on the physical file content, different Python classes can be used to process files. In general, the BufferedIOBase is able to process any file, while TextIOBase is a specialized class dedicated to processing text files (i.e. files containing human-visible texts divided into lines using new-line markers). Thus, the streams can be divided into binary and text ones.

3. The following open() function syntax is used to open a file:
    open(file_name, mode=open_mode, encoding=text_encoding)

The invocation creates a stream object and associates it with the file named file_name, using the specified open_mode and setting the specified text_encoding, or it raises an exception in the case of an error.

4. Three predefined streams are already open when the program starts:

    sys.stdin – standard input;
    sys.stdout – standard output;
    sys.stderr – standard error output.

5. The IOError exception object, created when any file operations fails (including open operations), contains a property named errno, which contains the completion code of the failed action. Use this value to diagnose the problem.
"""