segundos = int(input("digite um numero em segundos que será covertido para horas, minutos e segundos: "))

minutos = segundos / 60

horas = minutos / 60

print("o tempo em horas, minutos e segundos é igual a: ", horas,":",minutos,":",segundos)

# %%

segundos = float(input("digite um numero em segundos que será covertido para horas, minutos e segundos: "))

tempoDividido = segundos / 3600

print("o tempo em horas, minutos e segundos é igual a: ", tempoDividido)

# %% jeito que o teo fez

segundos = int(input("digite um numero em segundos que será covertido para horas, minutos e segundos: "))

horas = segundos // (60*60) # horas inteiras

segundos = segundos % (60*60) # resto dos segundos da divisao por hora

minutos = segundos // 60 # minutos inteiros

segundos = segundos % 60 # resto de segundos da divisao por minuto

print(horas, minutos, segundos, sep=":")
# %%
