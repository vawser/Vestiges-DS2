# -*- coding: utf-8 -*-
def talk_m10_23_7420():
    """Wandering warrior (hunting forest)"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_23_x9(z43=103651, z44=104150, z45=123020111)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            # talk:74205010:"Don't you ever give up!"
            call = talk_m10_23_x3(text9=74205010, z30=0, z31=20, z32=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                # talk:74205060:"Damn! This isn't right!"
                call = talk_m10_23_x6(z41=123020112, text16=74205060, text17=74205060, z42=74205060)
                if (HpValue() > 1) != 1:
                    pass
                elif KilledPlayer() != 0:
                    """State 5: [Lib] Killing state_SubState"""
                    Label('L1')
                    # talk:74205020:"Next time, you think before you pick a fight!\n"
                    talk_m10_23_x8(text18=74205020, z46=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                pass
            elif KilledPlayer() != 0:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Wandering Warrior: Conversation_SubState"""
                call = talk_m10_23_x45()
                if call.Done():
                    Continue('mainloop')
                elif (HpValue() > 1) != 1:
                    break
                elif KilledPlayer() != 0:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 7: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    # talk:74205030:"Whoah!", talk:74205040:"Hey, watch it there!", talk:74205050:"Why, you!"
                    call = talk_m10_23_x5(text20=74205030, text21=74205040, text22=74205050, text23=74205030,
                                          z48=123020115, z49=123020116)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        # talk:74205000:"Do you want some? Fine enough!"
                        call = talk_m10_23_x4(z50=103650, text24=74205000, z51=0, z52=103651)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            break
                        elif KilledPlayer() != 0:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(123020116) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(123020115) != 1:
                    Goto('L2')
        """State 6: [Lib] Death state_SubState"""
        # talk:74205070:"Aiiieegh!"
        talk_m10_23_x7(text19=74205070, z47=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_23_7700():
    """Darkness"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_23_x9(z43=103830, z44=104330, z45=123020131)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            # talk:77005010:"I cannot...let you have this."
            call = talk_m10_23_x3(text9=77005010, z30=0, z31=20, z32=80)
            if call.Done():
                """State 8: [Lib] Hostile state_SubState"""
                Label('L0')
                # talk:77005060:"Ahhhh...ahh...my...my...Dark\n"
                call = talk_m10_23_x6(z41=123020132, text16=77005060, text17=77005060, z42=77005060)
                if (HpValue() > 1) != 1:
                    pass
                elif KilledPlayer() != 0:
                    """State 5: [Lib] Killing state_SubState"""
                    Label('L1')
                    # talk:77005020:"One day...I will share your fate."
                    talk_m10_23_x8(text18=77005020, z46=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                pass
            elif KilledPlayer() != 0:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 10: Yakujuya: Conversation_SubState"""
                call = talk_m10_23_x46()
                if call.Done():
                    Continue('mainloop')
                elif (HpValue() > 1) != 1:
                    break
                elif KilledPlayer() != 0:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 7: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    # talk:77005030:"Hrk...", talk:77005040:"What are you doing?", talk:77005050:"Stop this."
                    call = talk_m10_23_x5(text20=77005030, text21=77005040, text22=77005050, text23=77005030,
                                          z48=123020135, z49=123020136)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First adversification_SubState"""
                        # talk:77005000:"You've let Dark...take control..."
                        call = talk_m10_23_x4(z50=103830, text24=77005000, z51=0, z52=0)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            break
                        elif KilledPlayer() != 0:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(123020136) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(123020135) != 1:
                    Goto('L2')
        """State 6: [Lib] Death state_SubState"""
        # talk:77005070:"Look...the Dark...I see it...I see it..."
        talk_m10_23_x7(text19=77005070, z47=0)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_23_7830():
    """Black phantom shop"""
    """State 0: Start state"""
    while Loop('mainloop'):
        """State 1: Conversation: Start"""
        if IsGuest() != 0:
            break
        else:
            pass
        """State 3: [Lib] Event: Branch_SubState"""
        call = talk_m10_23_x9(z43=103880, z44=104380, z45=123020121)
        if call.Get() == 1:
            """State 4: [Lib] Reunion hostility_SubState"""
            call = talk_m10_23_x3(text9=78309200, z30=0, z31=20, z32=80)
            if call.Done():
                """State 7: [Lib] Hostile state_SubState"""
                Label('L0')
                call = talk_m10_23_x6(z41=123020122, text16=78309500, text17=78309500, z42=78309500)
                if (HpValue() > 1) != 1:
                    pass
                elif KilledPlayer() != 0:
                    """State 5: [Lib] Killing state_SubState"""
                    Label('L1')
                    talk_m10_23_x8(text18=78309300, z46=0)
                    Quit()
            elif (HpValue() > 1) != 1:
                pass
            elif KilledPlayer() != 0:
                Goto('L1')
        elif call.Get() == 0:
            while True:
                """State 8: Black Phantom Shop: Conversation_SubState"""
                call = talk_m10_23_x38()
                if call.Done():
                    Continue('mainloop')
                elif (HpValue() > 1) != 1:
                    break
                elif KilledPlayer() != 0:
                    Goto('L1')
                elif (NumberOfTimesDamaged(1) > 3) != 0:
                    """State 6: [Lib] Hostile waiting_SubState"""
                    Label('L2')
                    call = talk_m10_23_x5(text20=78309400, text21=78309410, text22=78309420, text23=78309400,
                                          z48=123020125, z49=123020126)
                    if call.Done():
                        pass
                    elif (HpValue() > 1) != 1:
                        break
                    elif KilledPlayer() != 0:
                        Goto('L1')
                    elif (NumberOfTimesDamaged(1) > 3) != 0:
                        """State 9: [Lib] First hostility_ (pledge cancellation) _SubState"""
                        call = talk_m10_23_x15(z33=103880, text10=78309100, z34=0, val3=3, z35=200902,
                                               z36=0)
                        if call.Done():
                            Goto('L0')
                        elif (HpValue() > 1) != 1:
                            break
                        elif KilledPlayer() != 0:
                            Goto('L1')
                elif (NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(123020126) != 1:
                    Goto('L2')
                elif (NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(123020125) != 1:
                    Goto('L2')
        """State 10: [Lib] Death state_ (pledge cancellation) _SubState"""
        talk_m10_23_x35(text8=78309600, z20=0, val2=3)
        Quit()
    """State 2: Conversation: System: End"""
    EndMachine()

def talk_m10_23_x0(text11=_, z55=_, z56=0):
    """[Lib] Conversation: General purpose
    text11: Conversation ID
    z55: Conversation flag
    z56: Global event flag
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text11, GetCommonEventParamDecimal(7), -1)
    """State 6: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 5: Conversation: flag setting"""
    SetEventFlag(z55, 1)
    SetEventFlag(z56, 1)
    """State 7: Conversation: End"""
    return 0

def talk_m10_23_x1(text1=_, z34=_, z53=-1, z54=0):
    """[Lib] Conversation: Display only
    text1: Conversation ID
    z34: Conversation flag
    z53: Display distance
    z54: Global event flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text1, GetCommonEventParamDecimal(7), z53)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z34, 1)
    """State 5: Conversation: End"""
    return 0

def talk_m10_23_x2(text8=_, z20=0):
    """[Lib] Conversation: Event end
    text8: Conversation ID
    z20: Conversation flag
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text8, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z20, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_23_x3(text9=_, z30=0, z31=20, z32=80):
    """[Lib] Reunion hostility
    text9: Conversation message ID
    z30: Conversation flag ID
    z31: Display distance
    z32: Audible distance ratio
    """
    """State 0,1: Reunion hostility: start"""
    ClearNpcMenuResults()
    DeleteKeyGuideArea()
    """State 2: [Lib] Conversation: Hostile display only_SubState"""
    assert talk_m10_23_x27(text9=text9, z30=z30, z31=z31, z32=z32)
    """State 3: Reunion hostility: finished"""
    return 0

def talk_m10_23_x4(z50=_, text24=_, z51=0, z52=_):
    """[Lib] First hostility
    z50: Hostile: Global event flag
    text24: Conversation ID
    z51: Conversation flag
    z52: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z50, 1)
    SetEventFlag(z52, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z50) != 0 and GetEventFlag(103999) != 0
    """State 2: First hostility: save execution"""
    SaveExecution()
    assert ConversationEnded() != 0
    """State 3: Conversation: First hostilization_SubState"""
    assert talk_m10_23_x1(text1=text24, z34=z51, z53=-1, z54=0)
    """State 4: First hostility: end"""
    return 0

def talk_m10_23_x5(text20=_, text21=_, text22=_, text23=_, z48=_, z49=_):
    """[Lib] Hostile waiting
    text20: Conversation ID: 1 attacked
    text21: Conversation ID: Attacked 2
    text22: Conversation ID: 3 attacked
    text23: Conversation ID: 4 attacked
    z48: No use: Area and other flags
    z49: No, twice: Area and other flags
    """
    """State 0,1: Hostility: Start"""
    GenerateRandomNumber(0, 0, 100)
    DeleteKeyGuideArea()
    CancelConversation()
    """State 2: Hostility: Set damage flag"""
    SetEventFlagIf((NumberOfTimesDamaged(1) > 2) != 0 and GetEventFlag(z49) != 1, z49, 1)
    SetEventFlagIf((NumberOfTimesDamaged(1) > 1) != 0 and GetEventFlag(z48) != 1, z48, 1)
    """State 3: Hostility: Branch"""
    if (GetRandomValue(0) > 80 and GetRandomValue(0) < 100) != 0:
        """State 7: Conversation: 4_SubState attacked"""
        assert talk_m10_23_x1(text1=text23, z34=0, z53=-1, z54=0)
    elif (GetRandomValue(0) > 60 and GetRandomValue(0) < 80) != 0:
        """State 6: Conversation: Attacked 3_SubState"""
        assert talk_m10_23_x1(text1=text22, z34=0, z53=-1, z54=0)
    elif (GetRandomValue(0) > 40 and GetRandomValue(0) < 60) != 0:
        """State 5: Conversation: 2_SubState attacked"""
        assert talk_m10_23_x1(text1=text21, z34=0, z53=-1, z54=0)
    elif (GetRandomValue(0) > 20 and GetRandomValue(0) < 40) != 0:
        """State 4: Conversation: Attacked 1_SubState"""
        assert talk_m10_23_x1(text1=text20, z34=0, z53=-1, z54=0)
    else:
        pass
    """State 8: Hostility: End"""
    return 0

def talk_m10_23_x6(z41=_, text16=_, text17=_, z42=_):
    """[Lib] Hostile state
    z41: Area and other flags: HP decreased
    text16: Conversation ID: HP drop 1
    text17: Conversation ID: HP drop 2
    z42: Conversation ID: HP drop 3
    """
    """State 0,1: Hostile state: Start"""
    CancelConversation()
    while True:
        """State 2: Hostile state: standby"""
        BecomeHostile(1)
        assert (HpRatio() > 50) != 1 and GetEventFlag(z41) != 1 and ConversationEnded() != 0
        """State 3: Hostile state: HP decreased"""
        GenerateRandomNumber(0, 0, 30)
        if (GetRandomValue(0) > 0 and GetRandomValue(0) < 10) != 0:
            """State 4: Conversation: HP drop 1_SubState"""
            assert talk_m10_23_x10(text16=text16, z41=z41)
        elif (GetRandomValue(0) > 10 and GetRandomValue(0) < 20) != 0:
            """State 5: Conversation: HP drop 2_SubState"""
            assert talk_m10_23_x10(text16=text17, z41=z41)
        else:
            """State 6: Conversation: HP drop 3_SubState"""
            assert talk_m10_23_x10(text16=text17, z41=z41)

def talk_m10_23_x7(text19=_, z47=0):
    """[Lib] Death status
    text19: Conversation ID
    z47: Global: death flag
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: death message_SubState"""
    talk_m10_23_x2(text8=text19, z20=z47)

def talk_m10_23_x8(text18=_, z46=0):
    """[Lib] Murder status
    text18: Conversation ID
    z46: Conversation flag
    """
    """State 0,1: Killed state: Start"""
    DeleteKeyGuideArea()
    CancelConversation()
    assert ConversationEnded() != 0
    """State 2: Conversation: Killing message_SubState"""
    talk_m10_23_x2(text8=text18, z20=z46)

def talk_m10_23_x9(z43=_, z44=_, z45=_):
    """[Lib] Event: Branch
    z43: Hostile flag
    z44: death flag
    z45: Conversation start flag
    """
    """State 0,1: Event: Branch"""
    ClearNpcMenuResults()
    if GetEventFlag(z44) != 0:
        """State 2: Event: Ghosts: Waiting"""
        assert GetEventFlag(z45) != 0
    elif GetEventFlag(z43) != 0:
        """State 4: Event: End: Encounter Encounter"""
        return 1
    else:
        pass
    """State 3: Event: End: Normal encounter"""
    return 0

def talk_m10_23_x10(text16=_, z41=_):
    """[Lib] Conversation: HP drop
    text16: Conversation ID
    z41: Area and other flags: HP decreased
    """
    """State 0,1,2: Conversation: Message"""
    StartConversation(text16, GetCommonEventParamDecimal(7), -1)
    assert ConversationEnded() != 0
    """State 3: Conversation: Other area flag setting"""
    SetEventFlag(z41, 1)
    """State 4: Conversation: End"""
    return 0

def talk_m10_23_x11(action1=_):
    """[Lib] selection dialog
    action1: Dialog: Text ID
    """
    """State 0,1: Selection dialog: Display"""
    DisplayOwnYesNoMenu(action1, 0, -1, 0, 0, 0)
    assert YesNoMenuDisplay() != 0
    """State 2: Selection dialog: Waiting for input"""
    if (YesNoMenuResult() == 2) != 0:
        """State 4: End state: NO"""
        return 1
    elif (YesNoMenuResult() == 3) != 0:
        """State 5: End state: Cancel"""
        Label('L0')
        return 2
    elif YesNoMenuDisplay() != 1:
        Goto('L0')
    elif (YesNoMenuResult() == 1) != 0:
        """State 3: End state: YES"""
        return 0

def talk_m10_23_x12(z38=0, z39=220, z22=_, z40=0):
    """[Lib] Menu start: General purpose
    z38: Camera parameter ID
    z39: Target Damipoly ID
    z22: NPC event parameter ID
    z40: Cancel distance
    """
    """State 0,1,2: Menu start: Open"""
    OpenNpcMenu(z40, z38, z39, z22)
    """State 3: Menu start: Standby"""
    if (NpcMenuResult() == 19) != 0:
        """State 6: Cancel: End state"""
        return 0
    elif (NpcMenuResult() == 18) != 0:
        """State 7: Normal: End state"""
        Label('L0')
        return 1
    elif (NpcMenuResult() == 17) != 0:
        Goto('L0')
    elif (NpcMenuResult() == 16) != 0:
        """State 8: Conversation: end state"""
        return 2
    elif (NpcMenuResult() == 5) != 0:
        """State 12: Pledge: End state"""
        return 6
    elif (NpcMenuResult() == 9) != 0:
        """State 13: Immunity: End State"""
        return 7
    elif (NpcMenuResult() == 10) != 0:
        """State 9: Pledge Discard: End State"""
        return 3
    elif (NpcMenuResult() == 6) != 0:
        """State 10: Votive: End State"""
        return 4
    elif (NpcMenuResult() == 12) != 0:
        """State 11: Ladder: End state"""
        return 5
    elif (NpcMenuResult() == 13) != 0:
        """State 15: Route switching: End state"""
        return 9
    elif (NpcMenuResult() == 14) != 0:
        """State 14: Pass XX: End state"""
        return 8
    elif (NpcMenuResult() == 11) != 0:
        """State 16: Gesture: End state"""
        return 10
    elif (NpcMenuResult() == 1) != 0:
        """State 17: Point reassignment: end state"""
        return 11
    elif (NpcMenuResult() == 20) != 0:
        """State 18: Est bottle enhancement: end state"""
        return 12
    elif (NpcMenuResult() == 21) != 0:
        """State 19: Level up: End state"""
        return 13

def talk_m10_23_x13(text14=_, text15=_):
    """[Lib] Menu exit: General purpose
    text14: Conversation ID (at the time of purchase)
    text15: Conversation ID (when not purchased)
    """
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    if NpcMenuDisplay() != 1 and NpcMenuUsageResult() != 0:
        """State 2: Purchase and leave _SubState"""
        assert talk_m10_23_x1(text1=text14, z34=0, z53=-1, z54=0)
    elif NpcMenuDisplay() != 1:
        """State 3: Leave without purchase _SubState"""
        assert talk_m10_23_x1(text1=text15, z34=0, z53=-1, z54=0)
    """State 4: End state"""
    return 0

def talk_m10_23_x14(text13=_):
    """[Lib] Menu cancellation: General purpose
    text13: Conversation ID (when away)
    """
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: When you leave the shop _SubState"""
    assert talk_m10_23_x1(text1=text13, z34=0, z53=-1, z54=0)
    """State 4: End state"""
    return 0

def talk_m10_23_x15(z33=103880, text10=78309100, z34=0, val3=3, z35=200902, z36=0):
    """[Lib] First hostility _ (pledge cancellation)
    z33: Hostile: Global event flag
    text10: Conversation ID
    z34: Conversation flag
    val3: Cancellation pledge name
    z35: Pledge cancellation: Global conversation flag
    z36: Hostile map: Global event flag
    """
    """State 0,1: First hostility: start"""
    EndPlayerActionRequest()
    SetEventFlag(z33, 1)
    SetEventFlag(z36, 1)
    SetEventFlag(103999, 1)
    ClearNpcMenuResults()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    DeleteKeyGuideArea()
    CancelConversation()
    assert GetEventFlag(z33) != 0 and GetEventFlag(103999) != 0
    """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
    call = talk_m10_23_x26(val2=val3)
    if call.Done() and (GetPlayerCovenant() == val3) != 0:
        """State 3: First hostility: pledge change"""
        ChangePlayerCovenantIf((GetPlayerCovenant() == val3) != 0, 0)
        assert (GetStateTime() >= 0) != 0
        """State 2: First hostility: save execution"""
        SaveExecution()
        assert ConversationEnded() != 0
    elif call.Done() and ConversationEnded() != 0:
        pass
    """State 4: Conversation: First hostilization_SubState"""
    assert talk_m10_23_x1(text1=text10, z34=z34, z53=-1, z54=0)
    """State 6: First hostility: end"""
    return 0

def talk_m10_23_x16(text7=_, z15=0, lot7=_, z16=_, z17=212, z18=60):
    """[Lib] Conversation: Pledge ranking
    text7: Ranking: Conversation ID
    z15: Ranking: Conversation flag
    lot7: Item lottery
    z16: Ranking transfer: Global event flag
    z17: Previous rank: Global variable
    z18: Current rank: Area variable
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 8: Ranking up dialog_SubState"""
    # action:1308:"Your devotion to your\ncovenant has deepened,\nand you have gained a rank."
    assert talk_m10_23_x17(action3=1308)
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    StartConversation(text7, GetCommonEventParamDecimal(7), -1)
    """State 5: Conversation: Message waiting"""
    assert ConversationEnded() != 0
    """State 6: Conversation: flag setting"""
    SetEventFlag(z15, 1)
    if CanGetItemLot(lot7, 1) != 1 and GetEventFlag(z16) != 1:
        """State 10: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_23_x36(z19=1011, lot1=lot7)
    elif GetEventFlag(z16) != 0:
        pass
    else:
        """State 9: Ranking item transfer_SubState"""
        assert talk_m10_23_x19(lot1=lot7, z1=z16)
        """State 7: Conversation: Area variable ⇒ Global variable"""
        SetGlobalVariable(z17, GetAreaVariable(z18))
    """State 11: End state"""
    return 0

def talk_m10_23_x17(action3=_):
    """[Lib] OK dialog
    action3: Text ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayOwnOkMenu(action3, 0, 0, -1, 0, 0, 0)
    assert OkMenuDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert OkMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_23_x18(lot6=1770000, z14=102780, text5=77007000, text6=77007010):
    """[Lib] Equipment transfer: Mes⇒Item⇒Mes
    lot6: Item lottery ID
    z14: Global event flag
    text5: First half: Conversation ID
    text6: Second half: Conversation ID
    """
    """State 0,1,2: Equipment transfer: First half of conversation _SubState"""
    call = talk_m10_23_x1(text1=text5, z34=0, z53=-1, z54=0)
    # lot:1770000:Sunset Staff
    if call.Done() and CanGetItemLot(lot6, 1) != 1:
        """State 5: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_23_x36(z19=1011, lot1=lot6)
    elif call.Done():
        """State 3: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_23_x19(lot1=lot6, z1=z14)
        """State 4: Equipment transfer: Second half of conversation _SubState"""
        assert talk_m10_23_x1(text1=text6, z34=0, z53=-1, z54=0)
    """State 6: End state"""
    return 0

def talk_m10_23_x19(lot1=_, z1=_):
    """[Lib] Item acquisition dialog
    lot1: Item lottery ID
    z1: Global flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z1, 1)
    AwardItem(lot1, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_23_x20(z37=123020134, text11=77000400, text12=77000500):
    """[Lib] Conversation: Greeting: Single
    z37: Area other flag: Contact flag
    text11: Text ID: Talk to_continuous
    text12: Text ID: Talking after a long time
    """
    """State 0,1: Greeting: Start"""
    GenerateRandomNumber(0, 0, 20)
    if GetEventFlag(z37) != 0:
        """State 3: Talk to_continuous_SubState"""
        assert talk_m10_23_x0(text11=text11, z55=0, z56=0)
    else:
        """State 4: Talk to _After a long time_SubState"""
        assert talk_m10_23_x0(text11=text12, z55=0, z56=0)
        """State 2: Long time no see: contact flag set"""
        SetEventFlag(z37, 1)
    """State 5: End state"""
    return 0

def talk_m10_23_x21(lot5=2003000, z9=102880, text3=78300800, text4=78300840, z10=0, z11=0, z12=0, z13=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes: Key
    lot5: Item lottery ID
    z9: Item transfer: Global event flag
    text3: First half: Conversation ID
    text4: Second half: Conversation ID
    z10: Conversation: Global conversation flag
    z11: Trophy acquisition: Area and other flags
    z12: Emigration permission: Global event flag
    z13: White Phantom Appearance: Global Event Flag
    """
    """State 0,1,2: Item transfer: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Item transfer: Waiting for key guide input"""
    assert ConversationRequest() != 0
    """State 4: Item transfer: Delete key guide"""
    DeleteKeyGuideArea()
    """State 6: Item transfer: First half of conversation_SubState"""
    call = talk_m10_23_x1(text1=text3, z34=0, z53=-1, z54=0)
    if call.Done() and GetEventFlag(z9) != 0:
        """State 5: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z10, 1)
        SetEventFlag(z12, 1)
        SetEventFlag(z13, 1)
        """State 7: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_23_x1(text1=text4, z34=0, z53=-1, z54=0)
    # lot:2003000:Crest of Blood
    elif call.Done() and CanGetItemLot(lot5, 1) != 1:
        """State 9: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_23_x36(z19=1011, lot1=lot5)
    elif call.Done():
        """State 8: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_23_x22(lot4=lot5, z6=z9, z7=z10, z8=z11, z12=z12, z13=z13)
        Goto('L0')
    """State 10: End state"""
    return 0

def talk_m10_23_x22(lot4=_, z6=_, z7=0, z8=0, z12=0, z13=0):
    """[Lib] Item acquisition dialog: Conversation
    lot4: Item lottery ID
    z6: Item transfer: Global event flag
    z7: Conversation: Global conversation flag
    z8: Trophy acquisition: Area and other flags
    z12: Emigration permission: Global event flag
    z13: White Phantom Appearance: Global Event Flag
    """
    """State 0,1: Item acquisition dialog: Display"""
    SetEventFlag(z13, 1)
    SetEventFlag(z12, 1)
    SetEventFlag(z8, 1)
    SetEventFlag(z7, 1)
    SetEventFlag(z6, 1)
    AwardItem(lot4, 1)
    assert ItemAwardDisplay() != 0
    """State 2: Item acquisition dialog: Wait"""
    assert ItemAwardDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_23_x23(lot4=_, z6=_, text1=_, text2=_, z7=0, z8=0):
    """[Lib] Conversation: Item transfer: Mes⇒Item⇒Mes
    lot4: Item lottery ID
    z6: Item transfer: Global event flag
    text1: First half: Conversation ID
    text2: Second half: Conversation ID
    z7: Conversation: Global conversation flag
    z8: Trophy acquisition: Area and other flags
    """
    """State 0,1,3: Item transfer: First half of conversation_SubState"""
    call = talk_m10_23_x1(text1=text1, z34=0, z53=-1, z54=0)
    if call.Done() and GetEventFlag(z6) != 0:
        """State 2: Item transfer: Conversation flag: Setting"""
        SetEventFlag(z7, 1)
        """State 4: Item transfer: Second half of conversation _SubState"""
        Label('L0')
        assert talk_m10_23_x1(text1=text2, z34=0, z53=-1, z54=0)
    elif call.Done() and CanGetItemLot(lot4, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_23_x36(z19=1011, lot1=lot4)
    elif call.Done():
        """State 5: [Lib] Item acquisition dialog: Conversation_SubState"""
        assert talk_m10_23_x22(lot4=lot4, z6=z6, z7=z7, z8=z8, z12=0, z13=0)
        Goto('L0')
    """State 7: End state"""
    return 0

def talk_m10_23_x24():
    """[Lib] Menu exit: No Mes"""
    """State 0,1: Menu exit: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 2: End state"""
    return 0

def talk_m10_23_x25():
    """[Lib] Menu canceled: No Mes"""
    """State 0,1,2: Cancel menu: Close"""
    CloseNpcMenu()
    assert NpcMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_23_x26(val2=3):
    """[Lib] Pledge cancellation: Overwrite
    val2: Main pledge: pledge type
    """
    """State 0,1: Overwrite: Start"""
    if (not GetPlayerCovenant()) != 0:
        pass
    elif (GetPlayerCovenant() == val2) != 1:
        pass
    else:
        """State 2: Overwrite: Release flag"""
        SetEventFlagIf((GetPlayerCovenant() == 1) != 0, 200900, 1)
        SetEventFlagIf((GetPlayerCovenant() == 2) != 0, 200901, 1)
        SetEventFlagIf((GetPlayerCovenant() == 3) != 0, 200902, 1)
        SetEventFlagIf((GetPlayerCovenant() == 4) != 0, 200903, 1)
        SetEventFlagIf((GetPlayerCovenant() == 5) != 0, 200904, 1)
        SetEventFlagIf((GetPlayerCovenant() == 6) != 0, 200905, 1)
        SetEventFlagIf((GetPlayerCovenant() == 7) != 0, 200906, 1)
        SetEventFlagIf((GetPlayerCovenant() == 8) != 0, 200907, 1)
        SetEventFlagIf((GetPlayerCovenant() == 9) != 0, 200908, 1)
    """State 3: End state"""
    return 0

def talk_m10_23_x27(text9=_, z30=0, z31=20, z32=80):
    """[Lib] Conversation: Hostile display only
    text9: Conversation ID
    z30: Conversation flag
    z31: Display distance
    z32: Audible distance ratio
    """
    """State 0,1,5: Conversation: Waiting for display"""
    assert 132004 and (CompareOwnEzStateFlag(3) == 10) != 0
    """State 2: Conversation: Message"""
    StartConversation(text9, GetCommonEventParamDecimal(7), z31)
    """State 4: Conversation: Wait for message"""
    assert ConversationEnded() != 0
    """State 3: Conversation: flag setting"""
    SetEventFlag(z30, 1)
    """State 6: Conversation: End"""
    return 0

def talk_m10_23_x28(goods1=63018000, z21=102403):
    """[Lib] Menu item: Gesture
    goods1: Gesture: Item ID
    z21: Gesture acquisition: Global event flag
    """
    """State 0,1,3: [Lib] Get gesture dialog_SubState"""
    assert talk_m10_23_x33(goods1=goods1, z21=z21)
    """State 2: Gesture: Exit"""
    CloseNpcMenu()
    ClearNpcMenuSelection()
    """State 4: End state"""
    return 0

def talk_m10_23_x29(val1=3, z3=8, lot3=0, z4=0, action1=1332, action2=1342, z5=123020127):
    """[Lib] Pledge conclusion: General purpose
    val1: Pledge type
    z3: Event action
    lot3: Item lottery ID
    z4: Item transfer: Global event flag
    action1: Pledge text
    action2: Overwriting pledge text
    z5: Trophy acquisition: Area and other flags
    """
    """State 0,1,2: Commitment: Trophy setting"""
    SetEventFlag(z5, 1)
    if (not GetPlayerCovenant()) != 0:
        """State 3: When not pledged: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_23_x11(action1=action1)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            """State 8: Multiplayer pledge prohibition confirmation dialog_SubState"""
            Label('L0')
            # action:1311:"Cannot enter covenant\nwith phantom present"
            assert talk_m10_23_x17(action3=1311)
        elif call.Get() == 0:
            """State 7: [Lib] Event action: Pledge_SubState"""
            Label('L1')
            assert talk_m10_23_x30(z3=z3, val1=val1, lot3=lot3, z4=z4) and ItemAwardDisplay() != 1
            """State 6: Pledge confirmation dialog _SubState"""
            # action:1301:"Entered covenant"
            assert talk_m10_23_x17(action3=1301)
            """State 10: Conclusion: End state"""
            return 1
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    else:
        """State 4: Under pledge: Pledge conclusion selection dialog_SubState"""
        call = talk_m10_23_x11(action1=action2)
        if call.Get() == 0 and (MultiplayerComparison(0, 1) > 1) != 0:
            Goto('L0')
        elif call.Get() == 0:
            """State 5: [Lib] Pledge cancellation: Overwrite_SubState"""
            assert talk_m10_23_x26(val2=val1)
            Goto('L1')
        elif call.Get() == 1:
            pass
        elif call.Get() == 2:
            pass
    """State 9: Suspended: End state"""
    return 0

def talk_m10_23_x30(z3=8, val1=3, lot3=0, z4=0):
    """[Lib] Event action: Pledge
    z3: Event action
    val1: Pledge type
    lot3: Item lottery ID
    z4: Item transfer: Global event flag
    """
    """State 0,1,2: IventAction: Motion_Play"""
    PlayerActionRequest(z3)
    assert PlayerIsInEventAction(z3) != 0
    """State 3: IventAction: Motion_Waiting"""
    # lot:0:No Item
    if PlayerIsInEventAction(z3) != 1 and CanGetItemLot(lot3, 1) != 1 and GetEventFlag(z4) != 1:
        """State 6: Event action: pledge"""
        Label('L0')
        ChangePlayerCovenant(val1)
        # lot:0:No Item
        if (GetPlayerCovenant() == val1) != 0 and CanGetItemLot(lot3, 1) != 1 and GetEventFlag(z4) != 1:
            """State 7: [Lib] Inventory full dialog: Item display_SubState"""
            assert talk_m10_23_x36(z19=1011, lot1=lot3)
        elif (GetPlayerCovenant() == val1) != 0:
            pass
    elif PlayerIsInEventAction(z3) != 1 and GetEventFlag(z4) != 0:
        Goto('L0')
    elif PlayerIsInEventAction(z3) != 1:
        """State 5: Event action: Pledge conclusion: Item transfer"""
        ChangePlayerCovenant(val1)
        SetEventFlag(z4, 1)
        # lot:0:No Item
        AwardItem(lot3, 1)
        assert (GetPlayerCovenant() == val1) != 0
    """State 4: IventAction: Motion_Finish"""
    EndPlayerActionRequest()
    assert PlayerIsInEventAction(z3) != 1
    """State 8: End state"""
    return 0

def talk_m10_23_x31(z24=3, z25=60, z26=212, z27=102881, z28=102882, z29=102883):
    """[Lib] Pledge: Rank up: Conversation: 1
    z24: Pledge: Pledge type
    z25: Current rank: Area variable
    z26: Previous rank: Global variable
    z27: Ranking 1: Item transfer: Global event flag
    z28: Ranking 2: Item transfer: Global event flag
    z29: Ranking 3: Item transfer: Global event flag
    """
    """State 0,1,2: Rank up: Rank ⇒ Area variable"""
    SetAreaVariable(z25, GetPlayerCovenantLevel(z24))
    assert (GetStateTime() >= 0) != 0
    """State 3: Rank up: Rank change judgment"""
    if ((GetGlobalVariable(z26) > GetAreaVariable(z25)) != 1 and (GetGlobalVariable(z26) == GetAreaVariable(z25))
        != 1):
        """State 6: Rank up: End state"""
        Label('L0')
        return 1
    elif ((GetGlobalVariable(z26) > GetAreaVariable(z25)) != 0 and (GetGlobalVariable(z26) == GetAreaVariable(z25))
          != 1):
        """State 4: Rank up: Area variable ⇒ Global variable: When decreasing"""
        SetGlobalVariable(z26, GetAreaVariable(z25))
    elif GetEventFlag(z27) != 1 and (GetGlobalVariable(z26) > 1) != 0:
        Goto('L0')
    elif GetEventFlag(z28) != 1 and (GetGlobalVariable(z26) > 2) != 0:
        Goto('L0')
    elif GetEventFlag(z29) != 1 and (GetGlobalVariable(z26) > 3) != 0:
        Goto('L0')
    else:
        pass
    """State 5: Not ranked up: End state"""
    return 0

def talk_m10_23_x32(goods1=63018000, z21=102403, z22=74200000, z23=74200001):
    """[Lib] NPC menu: Gesture alone
    goods1: Item: Event item
    z21: Item transfer: Global event flag
    z22: NPC menu: With gesture
    z23: NPC menu: No gesture
    """
    """State 0,1: Menu: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(z21) != 0:
        pass
    else:
        while True:
            """State 3: Menu: Branch"""
            # goods:63018000:"Fist pump" Gesture
            if (ItemCount(goods1, 1, 1, 0) > 1) != 0:
                break
            else:
                """State 4: [Lib] Menu start: With gesture_SubState"""
                call = talk_m10_23_x12(z38=0, z39=220, z22=z22, z40=0)
                if call.Get() == 10:
                    """State 8: [Lib] Menu item: Gesture_SubState"""
                    call = talk_m10_23_x28(goods1=goods1, z21=z21)
                    if call.Done():
                        continue
                    elif (NpcMenuResult() == 19) != 0:
                        pass
                elif call.Get() == 0:
                    pass
                elif call.Get() == 1:
                    """State 6: [Lib] Menu exit: No Mes_SubState"""
                    Label('L0')
                    assert talk_m10_23_x24()
                    Goto('L2')
            """State 7: [Lib] Menu canceled: No Mes_SubState"""
            Label('L1')
            assert talk_m10_23_x25()
            Goto('L2')
        """State 5: [Lib] Menu start: No gesture _SubState"""
        call = talk_m10_23_x12(z38=0, z39=220, z22=z23, z40=0)
        if call.Get() == 0:
            Goto('L1')
        elif call.Get() == 1:
            Goto('L0')
    """State 2: Menu: Exit"""
    Label('L2')
    ClearNpcMenuResults()
    """State 9: End state"""
    return 0

def talk_m10_23_x33(goods1=63018000, z21=102403):
    """[Lib] Get gesture dialog
    goods1: Item ID
    z21: Global flag
    """
    """State 0,1: Get gesture dialog: Display"""
    ShowGestureMenu(goods1, 0, -1)
    SetEventFlag(z21, 1)
    assert GestureMenuDisplay() != 0
    """State 2: Get gesture dialog: Wait"""
    assert GestureMenuDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_23_x34(lot2=2003000, z2=102880):
    """[Lib] Conversation: Item transfer: Item: Key
    lot2: Item lottery
    z2: Item transfer: Global event flag
    """
    """State 0,1,2: Conversation: key guide creation"""
    CreateKeyGuideArea(9, 600)
    """State 3: Conversation: waiting"""
    assert ConversationRequest() != 0
    """State 4: Conversation: Message"""
    DeleteKeyGuideArea()
    # lot:2003000:Crest of Blood
    if CanGetItemLot(lot2, 1) != 1:
        """State 6: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_23_x36(z19=1011, lot1=lot2)
    elif GetEventFlag(z2) != 1:
        """State 5: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_23_x19(lot1=lot2, z1=z2)
    else:
        pass
    """State 7: Conversation: End"""
    return 0

def talk_m10_23_x35(text8=78309600, z20=0, val2=3):
    """[Lib] Death status_ (pledge cancellation)
    text8: Conversation ID
    z20: Global: death flag
    val2: Pledge type
    """
    """State 0,1: Death status: Start"""
    EndPlayerActionRequest()
    DeleteKeyGuideArea()
    CloseNpcMenuIf(NpcMenuDisplay() != 0)
    CancelConversation()
    assert ConversationEnded() != 0
    """State 4: [Lib] Pledge cancellation: Overwrite_SubState"""
    call = talk_m10_23_x26(val2=val2)
    if call.Done() and (GetPlayerCovenant() == val2) != 0:
        """State 2: Death status: pledge change"""
        ChangePlayerCovenant(0)
        assert ConversationEnded() != 0
    elif call.Done() and ConversationEnded() != 0:
        pass
    """State 3: Conversation: death message_SubState"""
    talk_m10_23_x2(text8=text8, z20=z20)

def talk_m10_23_x36(z19=1011, lot1=_):
    """[Lib] Inventory full dialog: Item display
    z19: Text ID
    lot1: Item lottery ID
    """
    """State 0,1: OK dialog: Display"""
    DisplayItemAwardFailure(lot1, 0, -1)
    assert ItemAwardFailureDisplay() != 0
    """State 2: OK dialog: Wait"""
    assert ItemAwardFailureDisplay() != 1
    """State 3: End state"""
    return 0

def talk_m10_23_x37(lot1=2003000, z1=102880):
    """[Lib] Conversation: Item transfer: Item: NOKey
    lot1: Item lottery
    z1: Item transfer: Global event flag
    """
    """State 0,1: Conversation: Start"""
    # lot:2003000:Crest of Blood
    if CanGetItemLot(lot1, 1) != 1:
        """State 3: [Lib] Inventory full dialog: Item display_SubState"""
        assert talk_m10_23_x36(z19=1011, lot1=lot1)
    elif GetEventFlag(z1) != 1:
        """State 2: [Lib] Item acquisition dialog_SubState"""
        assert talk_m10_23_x19(lot1=lot1, z1=z1)
    else:
        pass
    """State 4: Conversation: End"""
    return 0

def talk_m10_23_x38():
    """Black Phantom Shop: Conversation"""
    """State 0: Start state"""
    while True:
        """State 1: Conversation: Start"""
        ClearNpcMenuResults()
        if (GetPlayerCovenant() == 3) != 0:
            """State 5: Black Phantom Shop: Pledge Conversation_SubState"""
            call = talk_m10_23_x40()
            if call.Get() == 0:
                """State 7: Black Phantom Shop: NPC Menu_SubState"""
                Label('L0')
                assert talk_m10_23_x44()
            elif call.Get() == 1:
                pass
        elif GetEventFlag(200902) != 0:
            break
        # goods:62110000:Token of Spite
        elif (ItemCount(62110000, 1, 1, 0) > 1) != 0:
            """State 6: Black Phantom Shop: Unpowed Conversation_SubState"""
            call = talk_m10_23_x39()
            if call.Done():
                pass
            # goods:62110000:Token of Spite
            elif GetEventFlag(102880) != 1 and (ItemCount(62110000, 1, 1, 0) > 1) != 1:
                continue
        else:
            """State 3: Black Phantom Shop: Proof of Malicious: Not Owned_SubState"""
            assert talk_m10_23_x41()
        """State 2: Conversation: End"""
        Label('L1')
        ClearNpcMenuResults()
        """State 8: End state"""
        return 0
    """State 4: Black Phantom Shop: Re-contract_SubState"""
    call = talk_m10_23_x42()
    if call.Get() == 0:
        Goto('L0')
    elif call.Get() == 1:
        Goto('L1')

def talk_m10_23_x39():
    """Black phantom shop: unpowed conversation"""
    """State 0,1: Unpowed conversation: Start"""
    if GetEventFlag(205600) != 0:
        """State 5: Talk to: Subsequent _SubState"""
        # talk:78300200:"You've done well to find me."
        assert talk_m10_23_x0(text11=78300200, z55=0, z56=0)
    else:
        """State 4: Talk: First Look _SubState"""
        # talk:78300100:"Ooh, welcome, welcome."
        assert talk_m10_23_x0(text11=78300100, z55=205600, z56=0)
    """State 6: Talk: First Look: Select Dialog_SubState"""
    # action:1205:"What is your choice?"
    call = talk_m10_23_x11(action1=1205)
    if call.Get() == 0:
        """State 7: Talk to: YES1_SubState"""
        # talk:78300300:"Yes, of course,\nwhy else would you be here?"
        assert talk_m10_23_x1(text1=78300300, z34=0, z53=-1, z54=0)
        """State 8: Speak: YES1: Select dialog_SubState"""
        # action:1205:"What is your choice?"
        call = talk_m10_23_x11(action1=1205)
        if call.Get() == 0:
            """State 9: Talk: YES2: 1_SubState"""
            # talk:78300400:"Then you will need blood, lots of it."
            assert talk_m10_23_x1(text1=78300400, z34=0, z53=-1, z54=0)
            """State 14: Speak: YES2: 2_SubState"""
            # talk:78300420:"But it's not as easy as you think! Nah hah hah..."
            assert talk_m10_23_x1(text1=78300420, z34=0, z53=-1, z54=0)
            """State 15: Speak: YES2: 3_SubState"""
            # talk:78300430:"Well, what'dya say? Join the Brotherhood of Blood?"
            assert talk_m10_23_x1(text1=78300430, z34=0, z53=-1, z54=0)
            """State 10: Speak: YES2: Select dialog_SubState"""
            # action:1205:"What is your choice?"
            call = talk_m10_23_x11(action1=1205)
            if call.Get() == 0:
                """State 2: Talk to: YES3_SubState"""
                # talk:78300500:"Hmm..."
                assert talk_m10_23_x1(text1=78300500, z34=0, z53=-1, z54=0)
                """State 11: [Lib] Pledge conclusion: General purpose_SubState"""
                # lot:0:No Item, action:1332:"Join the Brotherhood of Blood covenant?", action:1342:"Abandon your covenant and\njoin the Brotherhood of Blood?"
                call = talk_m10_23_x29(val1=3, z3=8, lot3=0, z4=0, action1=1332, action2=1342, z5=123020127)
                if call.Get() == 0 and GetEventFlag(205604) != 0:
                    """State 13: Talk to: NO: 2nd time_SubState"""
                    Label('L0')
                    # talk:78300700:"But if you seek Undead blood...I welcome you."
                    assert talk_m10_23_x1(text1=78300700, z34=0, z53=-1, z54=0)
                elif call.Get() == 0:
                    """State 3: Talk to: NO_SubState"""
                    Label('L1')
                    # talk:78300600:"Well, that's no fun..."
                    assert talk_m10_23_x1(text1=78300600, z34=205604, z53=-1, z54=0)
                elif call.Get() == 1:
                    """State 16: Talk to: pledge formation: 1_SubState"""
                    # talk:78300800:"Heh heh heh...\nI knew it, I knew it!"
                    assert talk_m10_23_x1(text1=78300800, z34=0, z53=-1, z54=0)
                    """State 12: Talk: Pledge formation: 2_SubState"""
                    # lot:2003000:Crest of Blood, talk:78300820:"Now you are a servant of Nahr Alma.", talk:78300840:"There! Another servant of blood is born!"
                    assert (talk_m10_23_x23(lot4=2003000, z6=102880, text1=78300820, text2=78300840,
                            z7=0, z8=0))
            elif call.Get() == 2 and GetEventFlag(205604) != 0:
                Goto('L0')
            elif call.Get() == 1 and GetEventFlag(205604) != 0:
                Goto('L0')
            elif call.Get() == 2:
                Goto('L1')
            elif call.Get() == 1:
                Goto('L1')
        elif call.Get() == 2 and GetEventFlag(205604) != 0:
            Goto('L0')
        elif call.Get() == 1 and GetEventFlag(205604) != 0:
            Goto('L0')
        elif call.Get() == 2:
            Goto('L1')
        elif call.Get() == 1:
            Goto('L1')
    elif call.Get() == 2 and GetEventFlag(205604) != 0:
        Goto('L0')
    elif call.Get() == 1 and GetEventFlag(205604) != 0:
        Goto('L0')
    elif call.Get() == 2:
        Goto('L1')
    elif call.Get() == 1:
        Goto('L1')
    """State 17: End state"""
    return 0

def talk_m10_23_x40():
    """Black Phantom Shop: Pledge conversation"""
    """State 0,1: Pledge conversation: start"""
    if GetEventFlag(102880) != 1:
        """State 9: [Lib] Conversation: Item transfer: Item: Key_SubState"""
        # lot:2003000:Crest of Blood
        assert talk_m10_23_x34(lot2=2003000, z2=102880)
    else:
        """State 5: [Lib] Pledge: Rank up: Conversation: 1_SubState"""
        call = talk_m10_23_x31(z24=3, z25=60, z26=212, z27=102881, z28=102882, z29=102883)
        if call.Get() == 1:
            """State 2: Rank up: Rank conversation judgment"""
            if (GetAreaVariable(60) > 1) != 0 and GetEventFlag(102881) != 1:
                """State 6: Conversation: Pledge Ranking 1_SubState"""
                # talk:78301900:"Heh heh, wow, you're something.", lot:2003011:Curved Twinblade
                assert talk_m10_23_x16(text7=78301900, z15=0, lot7=2003011, z16=102881, z17=212, z18=60)
                Goto('L0')
            elif (GetAreaVariable(60) > 2) != 0 and GetEventFlag(102882) != 1:
                """State 7: Conversation: Pledge Ranking 2_SubState"""
                # talk:78302000:"You're incredible, you really are.", lot:2003012:Crescent Sickle
                assert talk_m10_23_x16(text7=78302000, z15=0, lot7=2003012, z16=102882, z17=212, z18=60)
                Goto('L0')
            elif (GetAreaVariable(60) > 3) != 0 and GetEventFlag(102883) != 1:
                """State 8: Conversation: Pledge Ranking 3_SubState"""
                # talk:78302100:"I couldn't ask for anything more.", lot:2003013:Great Chaos Fireball
                assert talk_m10_23_x16(text7=78302100, z15=0, lot7=2003013, z16=102883, z17=212, z18=60)
                Goto('L0')
            else:
                pass
        elif call.Get() == 0:
            pass
        """State 3: Speak: _SubState after pledge"""
        # talk:78300900:"Well, how are we?"
        assert talk_m10_23_x0(text11=78300900, z55=0, z56=0)
        """State 10: Menu: Exit state"""
        return 0
    """State 11: Normal: End state"""
    Label('L0')
    return 1

def talk_m10_23_x41():
    """Black Phantom Shop: Proof of Malicious: Not Owned"""
    """State 0,2: First look: (no proof) _SubState"""
    # talk:78300000:"What is it?"
    call = talk_m10_23_x0(text11=78300000, z55=0, z56=0)
    if call.Done():
        pass
    # goods:62110000:Token of Spite
    elif (ItemCount(62110000, 1, 1, 0) > 1) != 0:
        """State 1: First look: Delete key guide"""
        DeleteKeyGuideArea()
    """State 3: End state"""
    return 0

def talk_m10_23_x42():
    """Black Phantom Shop: Re-contract"""
    """State 0,1: Re-contract: Start"""
    if GetEventFlag(205601) != 0:
        """State 4: Talk: Pledge re-contract_SubState"""
        # talk:78301300:"I've no use for you any more."
        assert talk_m10_23_x0(text11=78301300, z55=0, z56=0)
    else:
        """State 6: Speak: pledge re-contract: first time _SubState"""
        # talk:78301200:"Wait, you've left the Brotherhood of Blood."
        assert talk_m10_23_x0(text11=78301200, z55=205601, z56=0)
    """State 5: [Lib] Pledge conclusion: General purpose_SubState"""
    # lot:0:No Item, action:1332:"Join the Brotherhood of Blood covenant?", action:1342:"Abandon your covenant and\njoin the Brotherhood of Blood?"
    call = talk_m10_23_x29(val1=3, z3=8, lot3=0, z4=0, action1=1332, action2=1342, z5=123020127)
    if call.Get() == 0 and GetEventFlag(205604) != 0:
        """State 7: Talk to: pledge failure: second or later _SubState"""
        # talk:78300700:"But if you seek Undead blood...I welcome you."
        assert talk_m10_23_x1(text1=78300700, z34=0, z53=-1, z54=0)
    elif call.Get() == 0:
        """State 3: Talk to: pledge failure _SubState"""
        # talk:78300600:"Well, that's no fun..."
        assert talk_m10_23_x1(text1=78300600, z34=205604, z53=-1, z54=0)
    elif call.Get() == 1 and GetEventFlag(102880) != 1:
        """State 10: [Lib] Conversation: Item transfer: Item: NOKey_SubState"""
        # lot:2003000:Crest of Blood
        assert talk_m10_23_x37(lot1=2003000, z1=102880)
        """State 2: Talk: Pledge _SubState"""
        Label('L0')
        # talk:78301400:"Hmm... Not that I really care, but..."
        assert talk_m10_23_x1(text1=78301400, z34=0, z53=-1, z54=0)
    elif call.Get() == 1:
        Goto('L0')
    """State 12: Normal: End state"""
    return 1

def talk_m10_23_x43():
    """Black Phantom Shop: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if GetEventFlag(102890) != 1 and (GetPlayerCovenantLevel(3) > 3) != 0 and GetEventFlag(104380) != 1:
        """State 6: Equipment transfer (condition: pledge level MAX) _SubState"""
        # lot:1783040:Scythe of Nahr Alma
        assert talk_m10_23_x23(lot4=1783040, z6=102890, text1=78302200, text2=78302210, z7=0, z8=0)
    elif GetEventFlag(205603) != 0:
        """State 2: Menu conversation: Conversation flag initialization"""
        SetEventFlag(205602, 0)
        SetEventFlag(205603, 0)
        """State 4: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:78301000:"Know anything about Tokens of Spite?\nWell, you can fight other blood servants with them."
        assert talk_m10_23_x1(text1=78301000, z34=205602, z53=-1, z54=0)
    elif GetEventFlag(205602) != 0:
        """State 5: Menu conversation: 2_SubState"""
        # talk:78301100:"Have you heard of the Blue Sentinels?"
        assert talk_m10_23_x1(text1=78301100, z34=205603, z53=-1, z54=0)
    else:
        Goto('L0')
    """State 3: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 7: End state"""
    return 0

def talk_m10_23_x44():
    """Black phantom shop: NPC menu"""
    """State 0: Start state"""
    while True:
        """State 1,6: [Lib] Menu start: General purpose_SubState"""
        call = talk_m10_23_x12(z38=0, z39=220, z22=78300000, z40=0)
        if call.Get() == 2:
            """State 3: Black Phantom Shop: Menu conversation_SubState"""
            call = talk_m10_23_x43()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 0:
            break
        elif call.Get() == 1:
            """State 5: [Lib] Exit menu: General purpose_SubState"""
            # talk:78301500:"Come back soon. Heh heh heh...", talk:78301600:"Fine, either way. Heh heh heh..."
            assert talk_m10_23_x13(text14=78301500, text15=78301600)
        """State 2: Menu: Exit"""
        Label('L0')
        ClearNpcMenuSelection()
        """State 7: End state"""
        return 0
    """State 4: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:78301700:"Thirsting for blood? Heh heh heh..."
    assert talk_m10_23_x14(text13=78301700)
    Goto('L0')

def talk_m10_23_x45():
    """Wandering Warrior: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(203202) != 0:
        """State 6: Talk: 4_SubState"""
        # talk:74200300:"Pate, the man with the strange ring.\nWatch out for the slimy rat."
        call = talk_m10_23_x0(text11=74200300, z55=0, z56=0)
        if call.Done() and GetEventFlag(102405) != 1:
            """State 3: Conversation: Set migration permission flag"""
            SetEventFlag(102405, 1)
            if GetEventFlag(102405) != 0 and GetEventFlag(102403) != 1:
                """State 8: [Lib] NPC menu: Gesture alone_SubState"""
                Label('L0')
                # goods:63018000:"Fist pump" Gesture
                assert talk_m10_23_x32(goods1=63018000, z21=102403, z22=74200000, z23=74200001)
            elif GetEventFlag(102405) != 0:
                pass
        elif call.Done() and GetEventFlag(102403) != 1:
            Goto('L0')
        elif call.Done():
            pass
    elif GetEventFlag(203201) != 0:
        """State 5: Speak: Part 3_SubState"""
        # talk:74200200:"You be careful of him. Pate, I think he said."
        assert talk_m10_23_x0(text11=74200200, z55=203202, z56=0)
    elif GetEventFlag(203200) != 0:
        """State 4: Talk to: 2_SubState"""
        # talk:74200100:"I am Creighton, of Mirrah.\nI travel from land to land to hone my blade."
        assert talk_m10_23_x0(text11=74200100, z55=203201, z56=0)
    else:
        """State 7: [Lib] Conversation: General purpose_SubState"""
        # talk:74200000:"Who are you?"
        assert talk_m10_23_x0(text11=74200000, z55=203200, z56=0)
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 9: End state"""
    return 0

def talk_m10_23_x46():
    """Yakujuya: Conversation"""
    """State 0,1: Conversation: Start"""
    ClearNpcMenuResults()
    if GetEventFlag(205101) != 0:
        """State 4: [Lib] Conversation: Greeting: Single _SubState"""
        # talk:77000400:"You are...always welcome...yes...?", talk:77000500:"The Dark...watches over you..."
        assert talk_m10_23_x20(z37=123020134, text11=77000400, text12=77000500)
        """State 5: Darkness Shop: NPC Menu_SubState"""
        Label('L0')
        assert talk_m10_23_x48()
    else:
        """State 3: Yakujuya: First conversation_SubState"""
        call = talk_m10_23_x47()
        if call.Get() == 0:
            pass
        elif call.Get() == 1:
            Goto('L0')
    """State 2: Conversation: End"""
    ClearNpcMenuResults()
    """State 6: End state"""
    return 0

def talk_m10_23_x47():
    """Yakujuya: First conversation"""
    """State 0,1: First conversation: start"""
    if (GetPlayerStat(5, 1) > NpcInfoValue(7700, 0)) != 0 and (GetPlayerStat(6, 1) > NpcInfoValue(7700, 1)) != 0:
        """State 5: Talk: Part 1: More than status_SubState"""
        # talk:77000200:"The Dark stirs..."
        assert talk_m10_23_x0(text11=77000200, z55=205101, z56=0)
        """State 7: Menu: Exit state"""
        return 1
    elif GetEventFlag(205100) != 0:
        """State 4: Talk: Part 1: Status or less: Second time _SubState"""
        # talk:77000100:"Leave me alone."
        call = talk_m10_23_x0(text11=77000100, z55=0, z56=0)
        if call.Done():
            pass
        elif ((GetPlayerStat(5, 1) > NpcInfoValue(7700, 0)) != 0 and (GetPlayerStat(6, 1) > NpcInfoValue(7700,
              1)) != 0):
            """State 2: First conversation: Delete key guide"""
            Label('L0')
            DeleteKeyGuideArea()
    else:
        """State 3: Talk: Part 1: Status or less: 1st _SubState"""
        # talk:77000000:"I don't know who you are...But leave me be."
        call = talk_m10_23_x0(text11=77000000, z55=205100, z56=0)
        if call.Done():
            pass
        elif ((GetPlayerStat(5, 1) > NpcInfoValue(7700, 0)) != 0 and (GetPlayerStat(6, 1) > NpcInfoValue(7700,
              1)) != 0):
            Goto('L0')
    """State 6: Normal: End state"""
    return 0

def talk_m10_23_x48():
    """Dark Art Shop: NPC Menu"""
    """State 0: Start state"""
    while True:
        """State 1,3: [Lib] Menu start: General purpose_SubState"""
        call = talk_m10_23_x12(z38=0, z39=220, z22=77000000, z40=0)
        if call.Get() == 2:
            """State 6: Yakujuya: Menu conversation_SubState"""
            call = talk_m10_23_x49()
            if call.Done():
                continue
            elif (NpcMenuResult() == 19) != 0:
                break
        elif call.Get() == 0:
            break
        elif call.Get() == 1:
            """State 4: [Lib] Exit menu: General purpose_SubState"""
            # talk:77000600:"Come again...as you like...", talk:77000700:"No matter...the time will come..."
            assert talk_m10_23_x13(text14=77000600, text15=77000700)
        """State 2: Menu: Exit"""
        Label('L0')
        """State 7: End state"""
        return 0
    """State 5: [Lib] Menu cancellation: General purpose_SubState"""
    # talk:77000800:"Till we meet again."
    assert talk_m10_23_x14(text13=77000800)
    Goto('L0')

def talk_m10_23_x49():
    """Yakujuya: Menu conversation"""
    """State 0,1: Menu conversation: Start"""
    if (GetEventFlag(102780) != 1 and (GetPlayerStat(5, 1) > NpcInfoValue(7700, 2)) != 0 and (GetPlayerStat(6,
        1) > NpcInfoValue(7700, 3)) != 0 and GetEventFlag(104330) != 1):
        """State 8: Equipment transfer (Condition: Belief is more than a certain level) _SubState"""
        # lot:1770000:Sunset Staff, talk:77007000:"These...are for you...", talk:77007010:"Together, into the Dark..."
        assert talk_m10_23_x18(lot6=1770000, z14=102780, text5=77007000, text6=77007010)
    elif GetEventFlag(205113) != 0:
        """State 3: Menu conversation: initialization"""
        SetEventFlag(205110, 0)
        SetEventFlag(205111, 0)
        SetEventFlag(205112, 0)
        SetEventFlag(205113, 0)
        """State 4: Menu conversation: Part 1_SubState"""
        Label('L0')
        # talk:77000900:"This land...lies closest to the Dark...\nTh-that is...that is why I came here."
        assert talk_m10_23_x1(text1=77000900, z34=205110, z53=-1, z54=0)
    elif GetEventFlag(205112) != 0:
        """State 7: Menu conversation: 4_SubState"""
        # talk:77001200:"What drew me to the Dark...I...I...I do not know."
        assert talk_m10_23_x1(text1=77001200, z34=205113, z53=-1, z54=0)
    elif GetEventFlag(205111) != 0:
        """State 6: Menu conversation: 3_SubState"""
        # talk:77001100:"Hexes originated in...ancient times."
        assert talk_m10_23_x1(text1=77001100, z34=205112, z53=-1, z54=0)
    elif GetEventFlag(205110) != 0:
        """State 5: Menu conversation: 2_SubState"""
        # talk:77001000:"I w-went...I went...I went to a great school...in the south...\nBut neither sorcery nor pyromancy appealed...I..."
        assert talk_m10_23_x1(text1=77001000, z34=205111, z53=-1, z54=0)
    else:
        Goto('L0')
    """State 2: Menu conversation: End"""
    ClearNpcMenuSelection()
    """State 9: End state"""
    return 0

