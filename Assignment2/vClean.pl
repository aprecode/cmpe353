:-dynamic at_room/1, dirty/1, point/1.
:-retractall(at_room(_)).


at_room(a).

point(0).

dirty(a).
dirty(b).
dirty(c).
dirt(d).

path(a,r,b).
path(b,l,a).
path(b,d,c).
path(c,u,b).
path(c,r,d).
path(d,l,c).


movement :-
  point(Number),
  New is Number - 1,
  retract(point(Number)),
  assert(point(New)),
  write('-1 point for movement.'), nl,
  write('Point is: '),
  write(New).

prize :-
  point(Numb),
  New is Numb + 2,
  retract(point(Numb)),
  assert(point(New)),
  write('+ 2 points for clean room.'), nl,
  write('Point is: '),
  write(New).


suck :-
  at_room(Room),
  dirty(Room),
  retract(dirty(Room)),
  write('Room is clean now '),
  prize,
  nl, !.

suck :-
  write('Room is not dirty '), nl.

r :- go(r).
l :- go(l).
d :- go(d).
u :- go(u).

go(Direction) :-
  movement,
  at_room(Here),
  path(Here, Direction, There),
  retract(at_room(Here)),
  assert(at_room(There)),
  look, !.

go(_) :-
  write('Bump'), nl,
  look.

look :-
  at_room(Room),
  describe(Room),
  nl.



describe(a) :-
  nl,
  at_room(a),
  dirty(a),
  write('You are in room A'), nl,
  write('Room A is dirty'), nl.

describe(a) :-
  nl,
  at_room(a),
  write('You are in room A'), nl,
  write('Room A is clean'), nl.



/* Describe the status of all rooms */
describe(b) :-
  nl,
  at_room(b),
  dirty(b),
  write('You are in room B'), nl,
  write('Room B is dirty'), nl.

describe(b) :-
  nl,
  at_room(b),
  write('You are in room B'), nl,
  write('Room B is clean'), nl.

describe(c) :-
  nl,
  at_room(c),
  dirty(c),
  write('You are in room C'), nl,
  write('Room C is dirty'), nl.

describe(c) :-
  nl,
  at_room(c),
  write('You are in room C'), nl,
  write('Room C is clean'), nl.

describe(d) :-
  nl,
  at_room(d),
  dirty(d),
  write('You are in room D'), nl,
  write('Room D is dirty'), nl.

describe(d) :-
  nl,
  at_room(d),
  write('You are in room D'), nl,
  write('Room D is clean'), nl.


stop :-
  dirty(a),
  dirty(b),
  dirty(c),
  dirty(d),
  write('All rooms must be cleaned'), nl.

stop :-
  nl,
  write('All rooms are clean'), nl,
  write('Final point is: '),
  write(point),
  nl, !.


instructions :-
  nl,
  write('Actions are: '), nl,
  write('r: Right, l: Left d: Down, u: Up -- for the direction'), nl,
  write('suck -- to suck the dirt in the room'), nl,
  write('stop -- to stop the vacuum cleaner when all the rooms are clean'), nl,
  write('look -- discribe the room'), nl,
  write('instructions -- to see the instructions again'), nl,
  write('Every movement will be penalized with -1 point'), nl,
  write('Agent will get +2 points for every time when a room is cleaned'),
  nl.

start :-
  instructions,
  look.






