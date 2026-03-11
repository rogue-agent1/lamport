#!/usr/bin/env python3
"""Lamport logical timestamps."""
import sys
class LamportClock:
    def __init__(self,pid): self.time=0; self.pid=pid
    def tick(self): self.time+=1; return self.time
    def send(self): return self.tick()
    def receive(self,sender_time): self.time=max(self.time,sender_time)+1; return self.time
events=[]
p0,p1,p2=LamportClock(0),LamportClock(1),LamportClock(2)
events.append(('P0','local',p0.tick()))
events.append(('P0','send→P1',p0.send()))
t=events[-1][2]
events.append(('P1','recv←P0',p1.receive(t)))
events.append(('P1','local',p1.tick()))
events.append(('P1','send→P2',p1.send()))
t=events[-1][2]
events.append(('P2','recv←P1',p2.receive(t)))
events.append(('P0','local',p0.tick()))
events.append(('P2','send→P0',p2.send()))
t=events[-1][2]
events.append(('P0','recv←P2',p0.receive(t)))
print("Lamport Timestamps:")
for proc,event,ts in events: print(f"  {proc} t={ts:2d}: {event}")
