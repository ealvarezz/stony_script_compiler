
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftNOTleftLTLEEQNEGTGEleftINleftPLUSMINUSleftFLOORleftMODleftTIMESDIVIDErightPOWleftLBRACKETleftLBRACEAND ASSIGN BOOL COMMA DIVIDE ELSE EQ FLOOR GE GT IF IN LBRACE LBRACKET LE LPAREN LT MINUS MOD NE NOT NUMBER OR PLUS POW PRINT RBRACE RBRACKET RPAREN SEMI STRING TIMES VARNAME WHILE\n    root : LBRACE stmt_list RBRACE\n    \n    stmt : LBRACE stmt_list RBRACE\n    \n    stmt_list : stmt stmt_list\n    \n    stmt_list :\n    \n    stmt : PRINT LPAREN expr  RPAREN SEMI\n    \n    stmt : VARNAME ASSIGN expr SEMI\n    \n    stmt : VARNAME ASSIGN VARNAME SEMI\n    \n    stmt : VARNAME LBRACKET expr RBRACKET ASSIGN expr SEMI\n    \n    stmt : expr LBRACKET expr RBRACKET ASSIGN expr SEMI\n         | STRING  LBRACKET expr RBRACKET ASSIGN expr SEMI\n    \n    stmt : WHILE LPAREN expr RPAREN LBRACE stmt_list  RBRACE\n    \n     stmt : IF LPAREN expr RPAREN LBRACE stmt_list RBRACE\n    \n    stmt : IF LPAREN expr RPAREN LBRACE stmt_list RBRACE ELSE LBRACE stmt_list RBRACE\n    \n    expr : VARNAME LBRACKET expr RBRACKET\n    \n    expr : expr PLUS expr\n         | expr MINUS expr\n         | expr TIMES expr\n         | expr DIVIDE expr\n         | expr FLOOR expr\n         | expr MOD expr\n         | expr POW expr\n    \n    expr : expr AND expr\n         | expr OR expr\n         | expr GT expr\n         | expr GE expr\n         | expr EQ expr\n         | expr LT expr\n         | expr LE expr\n         | expr NE expr\n    \n    expr : LBRACKET items RBRACKET\n    \n    items : items COMMA expr\n    \n    items : expr\n    \n    expr : expr LBRACKET expr RBRACKET\n         | STRING LBRACKET expr RBRACKET\n    \n    expr : LBRACKET RBRACKET\n    \n    expr : LPAREN expr RPAREN\n    \n    expr : NOT expr\n    \n    expr : VARNAME\n    \n    expr : STRING\n    \n    expr : NUMBER\n    \n    expr : BOOL\n    \n    expr : expr IN expr\n    '
    
_lr_action_items = {'LBRACE':([0,2,3,5,50,86,87,91,92,93,100,101,107,108,109,110,111,112,113,115,],[2,3,3,3,-2,-7,-6,100,101,-5,3,3,-9,-8,-10,-11,-12,113,3,-13,]),'$end':([1,18,],[0,-1,]),'RBRACE':([2,3,4,5,17,19,50,86,87,93,100,101,105,106,107,108,109,110,111,113,114,115,],[-4,-4,18,-4,50,-3,-2,-7,-6,-5,-4,-4,110,111,-9,-8,-10,-11,-12,-4,115,-13,]),'PRINT':([2,3,5,50,86,87,93,100,101,107,108,109,110,111,113,115,],[6,6,6,-2,-7,-6,-5,6,6,-9,-8,-10,-11,-12,6,-13,]),'VARNAME':([2,3,5,7,10,14,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,46,47,48,50,53,54,55,77,86,87,93,97,98,99,100,101,107,108,109,110,111,113,115,],[9,9,9,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,73,22,22,22,22,-2,22,22,22,22,-7,-6,-5,22,22,22,9,9,-9,-8,-10,-11,-12,9,-13,]),'STRING':([2,3,5,7,10,14,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,46,47,48,50,53,54,55,77,86,87,93,97,98,99,100,101,107,108,109,110,111,113,115,],[11,11,11,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-2,23,23,23,23,-7,-6,-5,23,23,23,11,11,-9,-8,-10,-11,-12,11,-13,]),'WHILE':([2,3,5,50,86,87,93,100,101,107,108,109,110,111,113,115,],[12,12,12,-2,-7,-6,-5,12,12,-9,-8,-10,-11,-12,12,-13,]),'IF':([2,3,5,50,86,87,93,100,101,107,108,109,110,111,113,115,],[13,13,13,-2,-7,-6,-5,13,13,-9,-8,-10,-11,-12,13,-13,]),'LBRACKET':([2,3,5,7,8,9,10,11,14,15,16,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,84,85,86,87,88,89,90,93,94,95,96,97,98,99,100,101,102,103,104,107,108,109,110,111,113,115,],[10,10,10,10,24,42,10,46,10,-40,-41,10,53,54,55,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,-35,53,10,10,10,53,-2,53,-36,10,10,10,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,54,53,53,-30,10,53,53,53,53,53,53,-33,-7,-6,-14,53,-34,-5,-33,-14,-34,10,10,10,10,10,53,53,53,-9,-8,-10,-11,-12,10,-13,]),'LPAREN':([2,3,5,6,7,10,12,13,14,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,46,47,48,50,53,54,55,77,86,87,93,97,98,99,100,101,107,108,109,110,111,113,115,],[7,7,7,20,7,7,47,48,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,-2,7,7,7,7,-7,-6,-5,7,7,7,7,7,-9,-8,-10,-11,-12,7,-13,]),'NOT':([2,3,5,7,10,14,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,46,47,48,50,53,54,55,77,86,87,93,97,98,99,100,101,107,108,109,110,111,113,115,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-2,14,14,14,14,-7,-6,-5,14,14,14,14,14,-9,-8,-10,-11,-12,14,-13,]),'NUMBER':([2,3,5,7,10,14,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,46,47,48,50,53,54,55,77,86,87,93,97,98,99,100,101,107,108,109,110,111,113,115,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-2,15,15,15,15,-7,-6,-5,15,15,15,15,15,-9,-8,-10,-11,-12,15,-13,]),'BOOL':([2,3,5,7,10,14,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,46,47,48,50,53,54,55,77,86,87,93,97,98,99,100,101,107,108,109,110,111,113,115,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-2,16,16,16,16,-7,-6,-5,16,16,16,16,16,-9,-8,-10,-11,-12,16,-13,]),'PLUS':([8,9,11,15,16,21,22,23,44,45,49,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,82,83,84,85,88,89,90,94,95,96,102,103,104,],[25,-38,-39,-40,-41,25,-38,-39,-35,25,25,25,-36,25,-15,-16,-17,-18,-19,-20,-21,25,25,25,25,25,25,25,25,25,-38,25,25,-30,25,25,25,25,25,25,-33,-14,25,-34,-33,-14,-34,25,25,25,]),'MINUS':([8,9,11,15,16,21,22,23,44,45,49,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,82,83,84,85,88,89,90,94,95,96,102,103,104,],[26,-38,-39,-40,-41,26,-38,-39,-35,26,26,26,-36,26,-15,-16,-17,-18,-19,-20,-21,26,26,26,26,26,26,26,26,26,-38,26,26,-30,26,26,26,26,26,26,-33,-14,26,-34,-33,-14,-34,26,26,26,]),'TIMES':([8,9,11,15,16,21,22,23,44,45,49,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,82,83,84,85,88,89,90,94,95,96,102,103,104,],[27,-38,-39,-40,-41,27,-38,-39,-35,27,27,27,-36,27,27,27,-17,-18,27,27,-21,27,27,27,27,27,27,27,27,27,-38,27,27,-30,27,27,27,27,27,27,-33,-14,27,-34,-33,-14,-34,27,27,27,]),'DIVIDE':([8,9,11,15,16,21,22,23,44,45,49,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,82,83,84,85,88,89,90,94,95,96,102,103,104,],[28,-38,-39,-40,-41,28,-38,-39,-35,28,28,28,-36,28,28,28,-17,-18,28,28,-21,28,28,28,28,28,28,28,28,28,-38,28,28,-30,28,28,28,28,28,28,-33,-14,28,-34,-33,-14,-34,28,28,28,]),'FLOOR':([8,9,11,15,16,21,22,23,44,45,49,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,82,83,84,85,88,89,90,94,95,96,102,103,104,],[29,-38,-39,-40,-41,29,-38,-39,-35,29,29,29,-36,29,29,29,-17,-18,-19,-20,-21,29,29,29,29,29,29,29,29,29,-38,29,29,-30,29,29,29,29,29,29,-33,-14,29,-34,-33,-14,-34,29,29,29,]),'MOD':([8,9,11,15,16,21,22,23,44,45,49,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,82,83,84,85,88,89,90,94,95,96,102,103,104,],[30,-38,-39,-40,-41,30,-38,-39,-35,30,30,30,-36,30,30,30,-17,-18,30,-20,-21,30,30,30,30,30,30,30,30,30,-38,30,30,-30,30,30,30,30,30,30,-33,-14,30,-34,-33,-14,-34,30,30,30,]),'POW':([8,9,11,15,16,21,22,23,44,45,49,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,82,83,84,85,88,89,90,94,95,96,102,103,104,],[31,-38,-39,-40,-41,31,-38,-39,-35,31,31,31,-36,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-38,31,31,-30,31,31,31,31,31,31,-33,-14,31,-34,-33,-14,-34,31,31,31,]),'AND':([8,9,11,15,16,21,22,23,44,45,49,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,82,83,84,85,88,89,90,94,95,96,102,103,104,],[32,-38,-39,-40,-41,32,-38,-39,-35,32,-37,32,-36,32,-15,-16,-17,-18,-19,-20,-21,-22,32,-24,-25,-26,-27,-28,-29,-42,-38,32,32,-30,32,32,32,32,32,32,-33,-14,32,-34,-33,-14,-34,32,32,32,]),'OR':([8,9,11,15,16,21,22,23,44,45,49,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,82,83,84,85,88,89,90,94,95,96,102,103,104,],[33,-38,-39,-40,-41,33,-38,-39,-35,33,-37,33,-36,33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-42,-38,33,33,-30,33,33,33,33,33,33,-33,-14,33,-34,-33,-14,-34,33,33,33,]),'GT':([8,9,11,15,16,21,22,23,44,45,49,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,82,83,84,85,88,89,90,94,95,96,102,103,104,],[34,-38,-39,-40,-41,34,-38,-39,-35,34,34,34,-36,34,-15,-16,-17,-18,-19,-20,-21,34,34,-24,-25,-26,-27,-28,-29,-42,-38,34,34,-30,34,34,34,34,34,34,-33,-14,34,-34,-33,-14,-34,34,34,34,]),'GE':([8,9,11,15,16,21,22,23,44,45,49,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,82,83,84,85,88,89,90,94,95,96,102,103,104,],[35,-38,-39,-40,-41,35,-38,-39,-35,35,35,35,-36,35,-15,-16,-17,-18,-19,-20,-21,35,35,-24,-25,-26,-27,-28,-29,-42,-38,35,35,-30,35,35,35,35,35,35,-33,-14,35,-34,-33,-14,-34,35,35,35,]),'EQ':([8,9,11,15,16,21,22,23,44,45,49,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,82,83,84,85,88,89,90,94,95,96,102,103,104,],[36,-38,-39,-40,-41,36,-38,-39,-35,36,36,36,-36,36,-15,-16,-17,-18,-19,-20,-21,36,36,-24,-25,-26,-27,-28,-29,-42,-38,36,36,-30,36,36,36,36,36,36,-33,-14,36,-34,-33,-14,-34,36,36,36,]),'LT':([8,9,11,15,16,21,22,23,44,45,49,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,82,83,84,85,88,89,90,94,95,96,102,103,104,],[37,-38,-39,-40,-41,37,-38,-39,-35,37,37,37,-36,37,-15,-16,-17,-18,-19,-20,-21,37,37,-24,-25,-26,-27,-28,-29,-42,-38,37,37,-30,37,37,37,37,37,37,-33,-14,37,-34,-33,-14,-34,37,37,37,]),'LE':([8,9,11,15,16,21,22,23,44,45,49,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,82,83,84,85,88,89,90,94,95,96,102,103,104,],[38,-38,-39,-40,-41,38,-38,-39,-35,38,38,38,-36,38,-15,-16,-17,-18,-19,-20,-21,38,38,-24,-25,-26,-27,-28,-29,-42,-38,38,38,-30,38,38,38,38,38,38,-33,-14,38,-34,-33,-14,-34,38,38,38,]),'NE':([8,9,11,15,16,21,22,23,44,45,49,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,82,83,84,85,88,89,90,94,95,96,102,103,104,],[39,-38,-39,-40,-41,39,-38,-39,-35,39,39,39,-36,39,-15,-16,-17,-18,-19,-20,-21,39,39,-24,-25,-26,-27,-28,-29,-42,-38,39,39,-30,39,39,39,39,39,39,-33,-14,39,-34,-33,-14,-34,39,39,39,]),'IN':([8,9,11,15,16,21,22,23,44,45,49,51,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,82,83,84,85,88,89,90,94,95,96,102,103,104,],[40,-38,-39,-40,-41,40,-38,-39,-35,40,40,40,-36,40,-15,-16,-17,-18,-19,-20,-21,40,40,40,40,40,40,40,40,-42,-38,40,40,-30,40,40,40,40,40,40,-33,-14,40,-34,-33,-14,-34,40,40,40,]),'ASSIGN':([9,85,88,90,],[41,97,98,99,]),'RBRACKET':([10,15,16,22,23,43,44,45,49,52,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,75,76,78,82,83,84,89,94,95,96,],[44,-40,-41,-38,-39,76,-35,-32,-37,-36,85,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-42,88,-30,90,94,95,96,-31,-33,-14,-34,]),'RPAREN':([15,16,21,22,23,44,49,51,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,79,80,94,95,96,],[-40,-41,52,-38,-39,-35,-37,81,-36,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-42,-30,91,92,-33,-14,-34,]),'COMMA':([15,16,22,23,43,44,45,49,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,89,94,95,96,],[-40,-41,-38,-39,77,-35,-32,-37,-36,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-42,-30,-31,-33,-14,-34,]),'SEMI':([15,16,22,23,44,49,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,76,81,94,95,96,102,103,104,],[-40,-41,-38,-39,-35,-37,-36,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-42,86,87,-30,93,-33,-14,-34,107,108,109,]),'ELSE':([111,],[112,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'root':([0,],[1,]),'stmt_list':([2,3,5,100,101,113,],[4,17,19,105,106,114,]),'stmt':([2,3,5,100,101,113,],[5,5,5,5,5,5,]),'expr':([2,3,5,7,10,14,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,46,47,48,53,54,55,77,97,98,99,100,101,113,],[8,8,8,21,45,49,51,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,78,79,80,82,83,84,89,102,103,104,8,8,8,]),'items':([10,],[43,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> LBRACE stmt_list RBRACE','root',3,'p_root','main.py',522),
  ('stmt -> LBRACE stmt_list RBRACE','stmt',3,'p_block_statement','main.py',529),
  ('stmt_list -> stmt stmt_list','stmt_list',2,'p_statement_list','main.py',536),
  ('stmt_list -> <empty>','stmt_list',0,'p_statement_list_empty','main.py',543),
  ('stmt -> PRINT LPAREN expr RPAREN SEMI','stmt',5,'p_print_statement','main.py',551),
  ('stmt -> VARNAME ASSIGN expr SEMI','stmt',4,'p_assign_statement','main.py',558),
  ('stmt -> VARNAME ASSIGN VARNAME SEMI','stmt',4,'p_assign_var_to_var_statement','main.py',565),
  ('stmt -> VARNAME LBRACKET expr RBRACKET ASSIGN expr SEMI','stmt',7,'p_assign_var_list','main.py',572),
  ('stmt -> expr LBRACKET expr RBRACKET ASSIGN expr SEMI','stmt',7,'p_assign_list_statement','main.py',579),
  ('stmt -> STRING LBRACKET expr RBRACKET ASSIGN expr SEMI','stmt',7,'p_assign_list_statement','main.py',580),
  ('stmt -> WHILE LPAREN expr RPAREN LBRACE stmt_list RBRACE','stmt',7,'p_while_statement','main.py',587),
  ('stmt -> IF LPAREN expr RPAREN LBRACE stmt_list RBRACE','stmt',7,'p_if_statement','main.py',595),
  ('stmt -> IF LPAREN expr RPAREN LBRACE stmt_list RBRACE ELSE LBRACE stmt_list RBRACE','stmt',11,'p_if_else_statement','main.py',603),
  ('expr -> VARNAME LBRACKET expr RBRACKET','expr',4,'p_name_expression_index','main.py',611),
  ('expr -> expr PLUS expr','expr',3,'p_expression_binop','main.py',618),
  ('expr -> expr MINUS expr','expr',3,'p_expression_binop','main.py',619),
  ('expr -> expr TIMES expr','expr',3,'p_expression_binop','main.py',620),
  ('expr -> expr DIVIDE expr','expr',3,'p_expression_binop','main.py',621),
  ('expr -> expr FLOOR expr','expr',3,'p_expression_binop','main.py',622),
  ('expr -> expr MOD expr','expr',3,'p_expression_binop','main.py',623),
  ('expr -> expr POW expr','expr',3,'p_expression_binop','main.py',624),
  ('expr -> expr AND expr','expr',3,'p_expression_bincomp','main.py',631),
  ('expr -> expr OR expr','expr',3,'p_expression_bincomp','main.py',632),
  ('expr -> expr GT expr','expr',3,'p_expression_bincomp','main.py',633),
  ('expr -> expr GE expr','expr',3,'p_expression_bincomp','main.py',634),
  ('expr -> expr EQ expr','expr',3,'p_expression_bincomp','main.py',635),
  ('expr -> expr LT expr','expr',3,'p_expression_bincomp','main.py',636),
  ('expr -> expr LE expr','expr',3,'p_expression_bincomp','main.py',637),
  ('expr -> expr NE expr','expr',3,'p_expression_bincomp','main.py',638),
  ('expr -> LBRACKET items RBRACKET','expr',3,'p_expression_list','main.py',645),
  ('items -> items COMMA expr','items',3,'p_expression_list_item','main.py',652),
  ('items -> expr','items',1,'p_expression_last_item','main.py',660),
  ('expr -> expr LBRACKET expr RBRACKET','expr',4,'p_expression_index','main.py',667),
  ('expr -> STRING LBRACKET expr RBRACKET','expr',4,'p_expression_index','main.py',668),
  ('expr -> LBRACKET RBRACKET','expr',2,'p_expression_empty_list','main.py',675),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_expression_paren','main.py',682),
  ('expr -> NOT expr','expr',2,'p_expression_not','main.py',689),
  ('expr -> VARNAME','expr',1,'p_expression_variable','main.py',696),
  ('expr -> STRING','expr',1,'p_expression_string','main.py',703),
  ('expr -> NUMBER','expr',1,'p_expression_number','main.py',710),
  ('expr -> BOOL','expr',1,'p_expression_bool','main.py',717),
  ('expr -> expr IN expr','expr',3,'p_expression_in_list','main.py',724),
]
