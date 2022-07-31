
/* Some example facts
*/

knows(fred,dog).
knows(fred,book).
knows(dog,bone).
knows(mary,fred).
knows(fred,mary).
knows(dog,bowl).



/*


This code states that fred knows dog.
a predicate named knows is true for fred,dog

Type into the SWI-prolog console window

knows(fred,dog).

It should say true.
This is  a query, you're asking if fred knows his dog.

You have to end questions with a period.  If you type in:

knows(fred,dog)

SWI-Prolog will gove you a "|" prompt.  Typing in a period will
complete the question.


Type in:

knows(fred,W).

W is a variable (beacuse it starts with a capitol letter)
Prolog will respond with all the things that fred knows.
hit a ; to step through them until you get back to the ?- prompt.


Variables start with a capitol letter.

Type in:

knows(fred,w).

This will return false. Lowercase 'w' is not a variable and fred doesn't
know w.


A space between 'knows' and '(' is an error
other spaces are usually ok.

Type in:

knows (fred,mary).


Type in:

knows(bone,dog).

not true. dog knows bone.

Add
knows(dog,bowl).
to the list of facts at the top of the file.  Then save the
file and select Make from the Compile menu.  The console window should
mention that the file compiled. "knows(dog,bowl)." should now return
true.

More Prolog:

:-	if
,	and
;	or

% line comment



*/

awareOf(A,B) :-
	knows(A,C),
	knows(C,B).

/*

A is aware of B if A knows D and D knows B

try

awareOf(bone,mary).
awareOf(mary,dog).

*/

bachelor(P) :- male(P), not(married(P)).

male(henry).
male(tom).

married(tom).

/*
note all 'male' facts need to be listed together
if the source code is:

male(henry).
married(tom).
male(tom).

Then it will miss that tom is male.



Some math:
*/
positive(N) :- N>0.

non_zero(N) :- N<0 ; N>0.

square(In,Out) :-
	Out is In * In.


/*

can test with
square(4,W).

The predicate "N is E" will succeed whenever N is an unbound variable, and E is some arithmetic expression (like 2+3).

so square(W,4). will cause an error
because it will try '4 is W * W '  4 is not an unbound variable
and W * W is not some  arithmetic expression

=:=  - equals

=\=  - not equals

*/

factorial(0,1).

factorial(N,F) :-
   N>0,
   N1 is N-1,
   factorial(N1,F1),
   F is N * F1.


output :-
    write("The factorial is "),factorial(20,W),nl,write(W),nl.

:- initialization(output).

/*

factorial of 0 is 1

factorial of n is
  n * factorial of (n-1)  if n>0

factorial is a bunch of logical ANDs

factorial(-3,W).  will return false because N>0 is false

try factorial(3,W).

The lines:


output :-
    write("The factorial is "),factorial(20,W),nl,write(W),nl.

:- initialization(output).


will calculate the factorial of 20 when the file is compiled.  Uncomment
the lines and remake the file.

*/









