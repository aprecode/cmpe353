
guess_it :- 
  ttester(Instrument),
  write('Is this the instrument? '),
  write(Instrument),
  nl,
  undo.

ttester(guitar) :- 
  guitar, !.
ttester(ukulele) :- 
  ukulele, !.
ttester(violin) :- 
  violin, !.
ttester(cello) :- 
  cello, !.
ttester(saxophone) :- 
  saxophone, !.
ttester(panflute) :-
  panflute, !.
ttester(vuvuzela) :- 
  vuvuzela, !.
ttester(drum) :- 
  drum, !.
ttester(cajon) :- 
  cajon, !.
ttester(unknown). 



guitar :- 
  has_string,
  verify(has_six_strings),
  verify(has_frets).


ukulele :-
  has_string,
  verify(has_four_strings),
  verify(has_frets).


violin :- 
  bowed,
  verify(f_shaped_hole),
  verify(high_pitch).

cello :-
  bowed,
  verify(f_shaped_hole),
  verify(low_pitch).


saxophone :-
  wind,
  verify(has_holes),
  verify(has_many_pitch).

panflute :-
  wind,
  verify(have_holes).

vuvuzela :-
  wind,
  verify(have_no_holes).

drum :-
  percussion,
  noisy,
  verify(has_many_equipment).

cajon :-
  percussion,
  verify(no_drumstick).


  

has_string :- 
  verify(play_with_finger), !.

has_stirng :- 
  verify(has_frets),
  verify(play_with_pick).

bowed :- 
  verify(play_with_bow), !.

bowed :-
  has_string,
  verify(has_no_frets). 

wind :-
  verify(played_with_breath), !.

wind :-
  verify(has_cicle_holes).

percussion :-
  verify(makes_rhythm), !.

percussion :-
  verify(has_no_note).
 


ask(Question) :-
  write('Does the intrument has this feature: '),
  write(Question),
  write('? '),
  read(Response),
  nl,

  ((Response == yes ; Response == y) 
  	->
  	assert(yes(Question)) ;
  	assert(no(Question)), fail).

:- dynamic(yes/1, no/1).

verify(Q) :-
 (yes(Q) -> true ;
 (no(Q) -> fail ;
 ask(Q))).



undo :- 
  retract(yes(_)),
  fail. 

undo :- 
  retract(no(_)),
  fail.

undo.
  






