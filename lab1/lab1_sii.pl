% Diablo II LOD

act("Rogue Encampment").
act("Lut Gholein").
act("Kurast Docks").
act("Pandemonium Fortress").
act("Harrogath").

after("Lut Gholein", "Rogue Encampment").
after("Kurast Docks", "Lut Gholein").
after("Pandemonium Fortress", "Kurast Docks").
after("Harrogath", "Pandemonium Fortress").

boss("Andariel").
boss("Duriel").
boss("Mephisto").
boss("Diablo").
boss("Baal").

class("Amazon").
class("Necromancer").
class("Barbarian").
class("Sorceress").
class("Paladin").
class("Druid").
class("Assassin").

character_class("Amazon", "Rogue Encampment").
character_class("Necromancer", "Rogue Encampment").
character_class("Barbarian", "Harrogath").
character_class("Sorceress", "Lut Gholein").
character_class("Paladin", "Lut Gholein").
character_class("Druid", "Kurast Docks").
character_class("Assassin", "Kurast Docks").

boss_location("Andariel", "Rogue Encampment").
boss_location("Duriel", "Lut Gholein").
boss_location("Mephisto", "Kurast Docks").
boss_location("Diablo", "Pandemonium Fortress").
boss_location("Baal", "Harrogath").

% Финальный босс, если совпадает локация
is_final_boss(Boss, Act) :- 
    boss_location(Boss, Act), not((boss_location(OtherBoss, Act), OtherBoss \= Boss)).

% Можешшь победить, если локация класа и босса совпадают
can_defeat_boss(Class, Boss) :- 
    character_class(Class, Act), boss_location(Boss, Act).

% Переходишь, если победил финального босса и это следующий акт
unlocked_acts_after_boss(Act, Boss) :-
    is_final_boss(Boss, PrevAct), act(Act), Act \= PrevAct, after(Act, PrevAct).

% Классы в актах (распределены случайно)
available_classes_in_act(Class, Act) :-
    character_class(Class, Act).

% Боссы в локации (список)
bosses_in_act(BossList, Act) :-
    findall(Boss, boss_location(Boss, Act), BossList).





