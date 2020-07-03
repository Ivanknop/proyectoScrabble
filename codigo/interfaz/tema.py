import PySimpleGUI as sg

def mi_tema():
    sg.LOOK_AND_FEEL_TABLE['scrabble'] = {'BACKGROUND': '#4f280a', ##133d51',
                                            'TEXT': '#fff4c9',
                                            'INPUT': '#c7e78b',
                                            'TEXT_INPUT': '#000000',
                                            'SCROLL': '#c7e78b',
                                            'BUTTON': ('black', '#4f280a'),
                                            'PROGRESS': ('#01826B', '#D0D0D0'),
                                            'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                            }
    sg.theme('scrabble')