female(betsy).
female(diana).
female(britney).
female(jennet).

parent(albert, bob).
parent(albert, betsy).
parent(albert, bill).
 
parent(alice, bob).
parent(alice, betsy).
parent(alice, bill).
 
parent(bob, carl).
parent(bob, charlie).

dances(alice).


get_grandchild :-
  parent(albert,X),
  parent(X,Y),
  write('alberts grandchild is '),
  write(Y), nl.


get_grandparent :-
  parent(X,carl),
  parent(Y,X),
  write('carls grandparent is '),
  write(Y), nl.

get_gp :-
  parent(X, carl),
  parent(X,charlie),
  format('~w ~s grandparent ~n' , [X,"is the"]).


grand_parent(X,Y) :-
  parent(Z,X),
  parent(Y,Z).


blushes(X) :- human(X);
human(carl).

what_grade(5) :-
  write('go to kindergarten').

what_grade(6) :-
  write('go to first grade').

what_grade(Other) :-
  Grade is Other - 5,
  format('Go to grade ~w', [Grade]).





owns(albert, pet(cat, kiwi)).


customer(tom, smith, 22.33).
customer(sally, smith, 120.00).

get_cust_bal(Fname, Lname) :-
  customer(Fname,Lname,Bal),
  write(Fname), tab(1),
  format('~w owes $~2f ~n' ,[Lname, Bal]).



vertical(line(point(X,Y), point(X,Y2))).
horizontal(line(point(X,Y), point(X2,Y))).



warm_blooded(penguin).
warm_blooded(human).
 
produce_milk(penguin).
produce_milk(human).
 
have_feathers(penguin).
have_hair(human).
 
mammal(X) :-
  warm_blooded(X),
  produce_milk(X),
  have_hair(X).

related(X,Y) :-
  parent(X,Y).

related(X,Y) :-
  parent(X,Z),
  related(Z,Y).


% \+ (not)
% =:= (equal)
% =\= (unequal)
% ; (or_operation)


double_digit(X,Y) :-
  Y is X*2.


%random(0,100,x) **generates random value
%between(0,10,x) ** gives all the numbers btw 0-10
%abs(-10) (absolute val)
%max(10,20)
%min(20,4)
%round(4.52)
%truncate(3.14)
%floor(2.94)

% \= Not equal

%2** 5 (5th power of 2)
% // (integer division)

% writeq (prints string in btw quotes)


say_hey :-
  write('Who are you?'),
  read(X),
  write('Hey '),
  write(X).

fav_char :-
  write('What is your fav character? '),
  get(X),
  format('The ascii value ~w is ', [X]),
  put(X), nl.


write_to_file(File, Text) :-
  open(File, write, Stream),
  write(Stream,Text),
  close(Stream).

read_file(File) :-
  open(File,read,Stream),
  get_char(Stream, Char1),
  process_stream(Char1, Stream),
  close(Stream).


process_stream(end_of_file,_) :- !.

process_stream(Char, Stream) :-
  write(Char),
  get_char(Stream,Char2),
  process_stream(Char2,Stream).


count_to_10(10) :- write(10), nl.

count_to_10(X) :-
  write(X), nl,
  Y is X + 1,
  count_to_10(Y).


count_down(Low, High) :-
  between(Low, High, Y),
  Z is High - Y,
  write(Z), nl.


count_up(Low, High) :-
  between(Low, High, Y),
  Z is Y + Low,
  write(Z), nl.


guess_num :- loop(start).

loop(15) :- write('You guessed it').

loop(X) :-
  X \= 15,
  write('Guess number '),
  read(Guess),
  write(Guess),
  write(' is not the number'), nl,
  loop(Guess).


write_list([]).

write_list([H|T]) :-
  write(H), nl,
  write_list(T).


/* dfsdfs

dfsdfs*/













