# 2. NESTING LIST & DICTIONARIES
# FOR EXAMPLE :

#     {
#         Key : [List],          # Look here we put value itself as List and dictionary
#         Key2: {DICT},
#      }
# EXAMPLE :

capitals={
    "France":"PARIS",
    "Germany":"FRANCE",
}

# I) NESTED LIST IN DICTIONARY :

# travel_log_samp={
#     "FRANCE":"PARIS","Lile", "Dijon "       # Look THIS DOESN'T WORK BECAUSE EACH KEY CAN HAVE ONLY ONE VALUE
# }                                       # SOLN: SO ONLY WAY TO MAKETHIS 3 PIECES OF DATA OR VALUES IS BY TURNING IT INTO A LIST

# SOLN

travel_log={
    "FRANCE":["PARIS","LILE","DIJON"],
    "Germany":["Berlin","stuttgart"]

}
print(travel_log["FRANCE"][1])
#----------------------------------------------------------------
nested_list=["A","B",["C","D",["E","F","G"]]]
print(nested_list[2][2][2])
#---------------------------------------------------------------

#II) Nested Dictionary :    # To access something we always use square braces ~ Manocha

travel_log1={
    "France":{
        "num_time_visited":8,
        "Cities_visited":["Paris","Lile","Dijon"]
    } , # Look at comma
    "Germany":{
        "Cities_Visited":["Stuttgart","Berlin","Hamburg"],
        "total_visit":5
    }
}
                                                # ALWAYS REMEMBER MANOCHA
print(travel_log1["Germany"]["Cities_Visited"][0]) # To access something we always use square braces ~ Manocha
