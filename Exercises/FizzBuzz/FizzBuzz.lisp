(write-line "-- Fizz Buzz --") ; prints the header of the program.

(format t "Number: ")
(let ((userNumber (read))) ; reads a number from the user and binds it to the variable userNumber.
  (setq output "") ; initializes an new empty string variable
  (when (zerop (mod userNumber 3)) ; checks if the userNumber is divisible by 3 and concatenates "Fizz" to output if it is.
    (setq output (concatenate 'string output "Fizz"))
    )
  (when (zerop (mod userNumber 5)) ; same but for 5 and "Buzz"
    (setq output (concatenate 'string output "Buzz"))
    )
  (unless output ; checks if output is still an empty string.
    (setq output userNumber)) ; assigns the userNumber value to output if it is not divisible by 3 or 5.
  (format t "~a" output)) ; prints the final value of output.
