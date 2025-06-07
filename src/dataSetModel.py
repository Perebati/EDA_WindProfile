from sqlalchemy import func, DateTime, Double, create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
import matplotlib.pyplot as plt
import numpy as np
from datetime import timedelta
import pandas as pd
import csv

Base = declarative_base()

class DataSet(Base):
    __tablename__ = "DataSet"
    id = Column(DateTime, primary_key=True)
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    hour = Column(Integer)
    minute = Column(Integer)
    ws40 = Column(Double)
    ws50 = Column(Double)
    ws60 = Column(Double)
    ws70 = Column(Double)
    ws80 = Column(Double)
    ws90 = Column(Double)
    ws100 = Column(Double)
    ws110 = Column(Double)
    ws120 = Column(Double)
    ws130 = Column(Double)
    ws140 = Column(Double)
    ws150 = Column(Double)
    ws160 = Column(Double)
    ws170 = Column(Double)
    ws180 = Column(Double)
    ws190 = Column(Double)
    ws200 = Column(Double)
    ws220 = Column(Double)
    ws240 = Column(Double)
    ws260 = Column(Double)
    verts40 = Column(Double)
    verts50 = Column(Double)
    verts60 = Column(Double)
    verts70 = Column(Double)
    verts80 = Column(Double)
    verts90 = Column(Double)
    verts100 = Column(Double)
    verts110 = Column(Double)
    verts120 = Column(Double)
    verts130 = Column(Double)
    verts140 = Column(Double)
    verts150 = Column(Double)
    verts160 = Column(Double)
    verts170 = Column(Double)
    verts180 = Column(Double)
    verts190 = Column(Double)
    verts200 = Column(Double)
    verts220 = Column(Double)
    verts240 = Column(Double)
    verts260 = Column(Double)
    wdir40 = Column(Double)
    wdir50 = Column(Double)
    wdir60 = Column(Double)
    wdir70 = Column(Double)
    wdir80 = Column(Double)
    wdir90 = Column(Double)
    wdir100 = Column(Double)
    wdir110 = Column(Double)
    wdir120 = Column(Double)
    wdir130 = Column(Double)
    wdir140 = Column(Double)
    wdir150 = Column(Double)
    wdir160 = Column(Double)
    wdir170 = Column(Double)
    wdir180 = Column(Double)
    wdir190 = Column(Double)
    wdir200 = Column(Double)
    wdir220 = Column(Double)
    wdir240 = Column(Double)
    wdir260 = Column(Double)
    cis1 = Column(Double)
    cis2 = Column(Double)
    cis3 = Column(Double)
    cis4 = Column(Double)
    cis5 = Column(Double)
    cis6 = Column(Double)
    cis7 = Column(Double)
    cis8 = Column(Double)
    cis9 = Column(Double)
    cis10 = Column(Double)
    cis11 = Column(Double)
    cis12 = Column(Double)
    cis13 = Column(Double)
    cis14 = Column(Double)
    cis15 = Column(Double)
    cis16 = Column(Double)
    cis17 = Column(Double)
    cis18 = Column(Double)
    cis19 = Column(Double)

    def __init__(
        self,
        id,
        year,
        month,
        day,
        hour,
        minute,
        ws40,
        ws50,
        ws60,
        ws70,
        ws80,
        ws90,
        ws100,
        ws110,
        ws120,
        ws130,
        ws140,
        ws150,
        ws160,
        ws170,
        ws180,
        ws190,
        ws200,
        ws220,
        ws240,
        ws260,
        verts40,
        verts50,
        verts60,
        verts70,
        verts80,
        verts90,
        verts100,
        verts110,
        verts120,
        verts130,
        verts140,
        verts150,
        verts160,
        verts170,
        verts180,
        verts190,
        verts200,
        verts220,
        verts240,
        verts260,
        wdir40,
        wdir50,
        wdir60,
        wdir70,
        wdir80,
        wdir90,
        wdir100,
        wdir110,
        wdir120,
        wdir130,
        wdir140,
        wdir150,
        wdir160,
        wdir170,
        wdir180,
        wdir190,
        wdir200,
        wdir220,
        wdir240,
        wdir260,
        cis1,
        cis2,
        cis3,
        cis4,
        cis5,
        cis6,
        cis7,
        cis8,
        cis9,
        cis10,
        cis11,
        cis12,
        cis13,
        cis14,
        cis15,
        cis16,
        cis17,
        cis18,
        cis19,
    ):
        self.id = id
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.ws40 = ws40
        self.ws50 = ws50
        self.ws60 = ws60
        self.ws70 = ws70
        self.ws80 = ws80
        self.ws90 = ws90
        self.ws100 = ws100
        self.ws110 = ws110
        self.ws120 = ws120
        self.ws130 = ws130
        self.ws140 = ws140
        self.ws150 = ws150
        self.ws160 = ws160
        self.ws170 = ws170
        self.ws180 = ws180
        self.ws190 = ws190
        self.ws200 = ws200
        self.ws220 = ws220
        self.ws240 = ws240
        self.ws260 = ws260
        self.verts40 = verts40
        self.verts50 = verts50
        self.verts60 = verts60
        self.verts70 = verts70
        self.verts80 = verts80
        self.verts90 = verts90
        self.verts100 = verts100
        self.verts110 = verts110
        self.verts120 = verts120
        self.verts130 = verts130
        self.verts140 = verts140
        self.verts150 = verts150
        self.verts160 = verts160
        self.verts170 = verts170
        self.verts180 = verts180
        self.verts190 = verts190
        self.verts200 = verts200
        self.verts220 = verts220
        self.verts240 = verts240
        self.verts260 = verts260
        self.wdir40 = wdir40
        self.wdir50 = wdir50
        self.wdir60 = wdir60
        self.wdir70 = wdir70
        self.wdir80 = wdir80
        self.wdir90 = wdir90
        self.wdir100 = wdir100
        self.wdir110 = wdir110
        self.wdir120 = wdir120
        self.wdir130 = wdir130
        self.wdir140 = wdir140
        self.wdir150 = wdir150
        self.wdir160 = wdir160
        self.wdir170 = wdir170
        self.wdir180 = wdir180
        self.wdir190 = wdir190
        self.wdir200 = wdir200
        self.wdir220 = wdir220
        self.wdir240 = wdir240
        self.wdir260 = wdir260
        self.cis1 = cis1
        self.cis2 = cis2
        self.cis3 = cis3
        self.cis4 = cis4
        self.cis5 = cis5
        self.cis6 = cis6
        self.cis7 = cis7
        self.cis8 = cis8
        self.cis9 = cis9
        self.cis10 = cis10
        self.cis11 = cis11
        self.cis12 = cis12
        self.cis13 = cis13
        self.cis14 = cis14
        self.cis15 = cis15
        self.cis16 = cis16
        self.cis17 = cis17
        self.cis18 = cis18
        self.cis19 = cis19

    def getSession(self):
        engine = create_engine(
            "postgresql://root:root@localhost:5432/DataSet-PerfilVento"
        )
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    
    def generate_graph(self, grafName, startDate, endDate, alturas, arg, type, avg):
        avg_ws_period = self.args_data_period(self, startDate, endDate, alturas, arg, type, avg)

        if(avg == 1):
            plt.figure(figsize=(18, 10))
        else:
            num = ((endDate - startDate).days + 1) * 9
            plt.figure(figsize=(int(num), 10))

        for i, data in enumerate(avg_ws_period):
            label = f'Altura {alturas[i]}'
            plt.plot(data, label=label)

        plt.title(grafName)
        plt.xlabel('Horas')
        plt.ylabel('Velocidade do Vento')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
        plt.grid(True)
        plt.tight_layout()

        start_date = pd.to_datetime(startDate)
        num_points = len(avg_ws_period[0])
        date_range = pd.date_range(start=start_date, periods=num_points, freq='h')

        custom_xticks = date_range.strftime('%H:%M')

        plt.xticks(ticks=range(num_points), labels=custom_xticks, rotation=45, ha='right')

        plt.show()
    
    def args_data_period(self, startDate, endDate, alturas, arg, type, avg):
        avg_ws_period = []
        
        if(avg == 1):
            for altura in alturas:
                avg_ws_day_list = self.args_data_interval_avg(self, startDate, endDate, altura, arg, type) 
                avg_ws_period.append(avg_ws_day_list)
        else:
            for altura in alturas:
                avg_ws_day_list = self.args_data_interval(self, startDate, endDate, altura, arg, type) 
                avg_ws_period.append(avg_ws_day_list)
        
        return avg_ws_period

    def args_data_interval(self, startDate, endDate, altura, arg, type):
        avg_ws_interval= []
        num_dias = (endDate - startDate).days + 1
        for i in range(num_dias):
            dia_atual = startDate + timedelta(days=i)
            avg_ws_day = self.args_data_day(self, dia_atual.year, dia_atual.month, dia_atual.day, altura, arg, type)
            for i in range(0, 24):
                avg_ws_interval.append(avg_ws_day[i])
                
                
        return avg_ws_interval
    
    def args_data_interval_avg(self, startDate, endDate, altura, arg, type):
        avg_ws_interval = []
        num_dias = (endDate - startDate).days + 1
        for i in range(num_dias):
            dia_atual = startDate + timedelta(days=i)
            data = self.args_data_day(self, dia_atual.year, dia_atual.month, dia_atual.day, altura, arg, type)
            avg_ws_interval.append(data)
            
        if avg_ws_interval:
            num_elements = len(avg_ws_interval[0])
            avg_values = [0] * num_elements
            
            for i in range(num_elements):
                total = sum(sublist[i] for sublist in avg_ws_interval)
                avg_values[i] = total / num_dias
        
        return avg_values 
           
    def args_data_day(self, ano, mes, dia, altura, arg, type):
        data_arg_day = []
        
        if(type == 0):
            for i in range(0, 24):
                data_arg_day.append(self.args_avg_hour(self, ano, mes, dia, i, altura, arg))
        
        if(type == 1):
            for i in range(0, 24):
                data_arg_day.append(self.args_max_hour(self, ano, mes, dia, i, altura, arg))
        
        if(type == 2):
            for i in range(0, 24):
                data_arg_day.append(self.args_min_hour(self, ano, mes, dia, i, altura, arg))
                
        if(type == 3):
            for i in range(0, 24):
                data_arg_day.append(self.args_asc_avg_hour(self, ano, mes, dia, i, altura, arg))
                
        if(type == 4):
            for i in range(0, 24):
                data_arg_day.append(self.args_dsc_avg_hour(self, ano, mes, dia, i, altura, arg))
        if(type == 5):
            for i in range(0, 24):
                data_arg_day.append(self.args_avg_hour(self, ano, mes, dia, i, altura, arg))
            data_arg_day = self.post_process(data_arg_day)
                            
        return data_arg_day
    
    def args_max_hour(self, ano, mes, dia, hora, altura, arg):
        session = self.getSession(self)
        
        try:
            max_arg_hour = session.query(func.max((getattr(DataSet, f"{arg}{altura}")))).filter(
                DataSet.year == ano,
                DataSet.month == mes,
                DataSet.day == dia,
                DataSet.hour == hora
            ).scalar()

            session.commit()

            return max_arg_hour if max_arg_hour is not None else 0.0

        except Exception as e:
            session.rollback()
            raise e

        finally:
            session.close()
            
    def args_min_hour(self, ano, mes, dia, hora, altura, arg):
        session = self.getSession(self)
        
        try:
            min_arg_hour = session.query(func.min((getattr(DataSet, f"{arg}{altura}")))).filter(
                DataSet.year == ano,
                DataSet.month == mes,
                DataSet.day == dia,
                DataSet.hour == hora
            ).scalar()

            session.commit()

            return min_arg_hour if min_arg_hour is not None else 0.0

        except Exception as e:
            session.rollback()
            raise e

        finally:
            session.close()
    
    def args_avg_hour(self, ano, mes, dia, hora, altura, arg):
        session = self.getSession(self)
        
        try:
            avg_arg_hour = session.query(func.avg((getattr(DataSet, f"{arg}{altura}")))).filter(
                DataSet.year == ano,
                DataSet.month == mes,
                DataSet.day == dia,
                DataSet.hour == hora
            ).scalar()

            session.commit()

            return avg_arg_hour if avg_arg_hour is not None else 0.0

        except Exception as e:
            session.rollback()
            raise e

        finally:
            session.close()
            
    def args_asc_avg_hour(self, ano, mes, dia, hora, altura, arg):
        session = self.getSession(self)
        
        try:
            avg_arg_hour = session.query(func.avg((getattr(DataSet, f"{arg}{altura}")))).filter(
                DataSet.year == ano,
                DataSet.month == mes,
                DataSet.day == dia,
                DataSet.hour == hora,
                (getattr(DataSet, f"{arg}{altura}") > 0)
            ).scalar()

            session.commit()

            return avg_arg_hour if avg_arg_hour is not None else 0.0

        except Exception as e:
            session.rollback()
            raise e

        finally:
            session.close()
            
    def args_dsc_avg_hour(self, ano, mes, dia, hora, altura, arg):
        session = self.getSession(self)
        
        try:
            avg_arg_hour = session.query(func.avg((getattr(DataSet, f"{arg}{altura}")))).filter(
                DataSet.year == ano,
                DataSet.month == mes,
                DataSet.day == dia,
                DataSet.hour == hora,
                (getattr(DataSet, f"{arg}{altura}") < 0)
            ).scalar()

            session.commit()

            return avg_arg_hour if avg_arg_hour is not None else 0.0

        except Exception as e:
            session.rollback()
            raise e

        finally:
            session.close()
            
    def post_process(vetor):
        vetor_modificado = np.copy(vetor)

        limite_superior = 0.5
        limite_inferior = -0.5

        for i in range(1, len(vetor_modificado) - 1):
            if vetor_modificado[i] >= limite_superior:
                vetor_modificado[i] = limite_superior
            elif vetor_modificado[i] <= limite_inferior:
                vetor_modificado[i] = limite_inferior
                
        return vetor_modificado
    
    def generate_csv(self):
        session = self.getSession(self)
        try:
            all_data = session.query(DataSet).all()

            with open('dataset.csv', mode='w', newline='') as file:
                writer = csv.writer(file)

                writer.writerow([column.name for column in DataSet.__table__.columns])

                for row in all_data:
                    writer.writerow([getattr(row, column.name) for column in DataSet.__table__.columns])

            session.commit()

            print("Arquivo .csv criado com sucesso!")

        except Exception as e:
            session.rollback()
            raise e

        finally:
            session.close()