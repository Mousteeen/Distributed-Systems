# Distributed-Systems
Solutions for the Distributed Systems Lab.

# Ubersicht
Im Rahmen des Praktikums Verteilte Systeme soll eine fiktive Anwendung aus
dem Bereich des Robotik- bzw. Roboterfussball entwickelt werden.1 Dazu sollen die Technologien Sockets, Remote Procedure Calls (RPCs) sowie MessageOriented-Middleware (MOM) verwendet werden. Die Anwendung entsteht dabei
Schritt f¨ur Schritt und jede der unten stehenden Aufgaben erweitert das System
um eine Komponente oder Funktionalit¨at.
In mehreren Phasen wird jeweils ein Teil des in Abbildung 1 dargestelten Gesamtsystems erstellt.
Am Ende m¨ussen mehrere Roboter, die ¨uber einen Controller gesteuert werden,
mittels eines verteilten Leader-Election Algorithmus einen Kapit¨an w¨ahlen. Das
Gesamtsystem soll m¨oglichst robust sein und Auf¨alle einzelner Systeme, z.B.
eines Roboters, verkraften k¨onnen.

![image](https://github.com/Mousteeen/Distributed-Systems/assets/134636415/22e18811-4839-496b-ab14-c3d9d5c9cbfd)
