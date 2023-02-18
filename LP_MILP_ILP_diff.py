import gurobipy as gp
from gurobipy import GRB


try:   
    # create a new model
    m = gp.Model()

    # create variables
    # float variables
    # x = m.addVar(vtype=GRB.CONTINUOUS, name="x")
    # y = m.addVar(vtype=GRB.CONTINUOUS, name="y")

    # integer variables
    x = m.addVar(vtype=GRB.INTEGER, name="x")
    y = m.addVar(vtype=GRB.INTEGER, name="y") 

    # set objective
    m.setObjective(x + y, GRB.MAXIMIZE)

    # add constraint: -2x + 2 y >= 1
    m.addConstr(-2*x + 2*y >= 1, "c0")

    # add constraint: -8x+10y <= 13
    m.addConstr(-8*x + 10*y <= 13, "c1")

    # add constraint: x>=0
    m.addConstr(x >= 0, "c2")

    # add constraint: y>=0
    m.addConstr(y >= 0, "c3")

    # optimize model
    m.optimize()

    # print variable values
    for v in m.getVars():
        print('%s %g' % (v.VarName, v.X))
        
    # print Objective value
    print('Obj: %g' % m.ObjVal)
    
except gp.GurobiError as e:
    print('Error code ' + str(e.errno) + ': ' + str(e))

except AttributeError:
    print('Encountered an attribute error')
