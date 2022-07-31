basel(Num,Result) :- basel(Num,0,Result).

 basel(Num,Acc,Result) :-
        % Predicate: Num is greater than 1
        ( Num > 1 
        % Update accumalator
       -> Acc1 is Acc + (1/(Num*Num)),
          % Decrement iteration counter
          NextNum is Num-1,
          % Recusrive call
          basel(NextNum,Acc1,Result)
          % Final case
          ; Result is Acc + (1/(Num*Num))
).

output :-
    write("Basel Sum of 100: "),basel(100,X),write(X),nl.

:- initialization(output).