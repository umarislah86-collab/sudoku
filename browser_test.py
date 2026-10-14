from playwright.sync_api import sync_playwright
import json
from pathlib import Path
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1440,'height':1000});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto('http://127.0.0.1:3000');page.wait_for_selector('.cell');assert page.locator('.cell').count()==81;assert page.locator('.level').count()==10
 givens=json.loads(Path('/workspace/sudoku/puzzles.js').read_text().split('=',1)[1].rstrip(';\n'))[0]['givens'];empty=givens.index(0)
 cell=page.locator('.cell').nth(empty);cell.click();page.locator('#notes').click();page.keyboard.press('3');assert cell.locator('.pencil').inner_text().strip()=='3';page.locator('#undo').click();assert cell.inner_text()==''
 page.locator('#notes').click();page.keyboard.press('4');assert cell.inner_text()=='4';page.reload();assert page.locator('.cell').nth(empty).inner_text()=='4'
 page.locator('.cell').nth(empty).click();page.locator('#erase').click();assert page.locator('.cell').nth(empty).inner_text()==''
 before=page.evaluate("JSON.parse(localStorage.getItem('ego-check-v1')).states[0]")
 first_title=None
 for attempt in range(1,10):
  page.locator('#hint').click();assert page.locator('#modal').is_visible()
  title=page.locator('#modal-title').inner_text()
  if attempt==1:first_title=title
  if attempt==2:assert title!=first_title
  if attempt==9:assert title==first_title
  assert page.locator('#hints').inner_text()==str(attempt)
  page.locator('#modal-action').click()
  after=page.evaluate("JSON.parse(localStorage.getItem('ego-check-v1')).states[0]")
  assert after['values']==before['values'] and after['notes']==before['notes']
  assert page.locator('.cell').nth(empty).inner_text()==''
 assert page.locator('.cell.selected').count()==1
 page.reload();assert page.locator('#hints').inner_text()=='9'
 page.locator('.cell').nth(empty).click();page.keyboard.press('2');page.locator('#hint').click();page.locator('#close').click();page.locator('#undo').click();assert page.locator('.cell').nth(empty).inner_text()==''

 page.locator('#pause').click();assert page.locator('#overlay').is_visible();page.locator('#resume').click();assert not page.locator('#overlay').is_visible()
 page.locator('.level').nth(1).click();assert page.locator('#counter').inner_text()=='02 / 10';page.locator('.level').nth(0).click();assert page.locator('#hints').inner_text()=='10'
 page.locator('#reset').click();page.locator('#modal-action').click();assert page.locator('#hints').inner_text()=='0'
 solution=json.loads(Path('/workspace/sudoku/puzzles.js').read_text().split('=',1)[1].rstrip(';\n'))[0]['solution']
 for i,v in enumerate(givens):
  if not v:page.locator('.cell').nth(i).click();page.keyboard.press(str(solution[i]))
 assert page.locator('#modal-title').inner_text()=='Okay, memang hebat.';assert '✓' in page.locator('.level').nth(0).inner_text()
 page.locator('#close').click();page.locator('.level').nth(1).click();page.screenshot(path='/workspace/sudoku/desktop.png',full_page=True)
 page.set_viewport_size({'width':390,'height':844});assert page.evaluate('document.documentElement.scrollWidth <= innerWidth');page.screenshot(path='/workspace/sudoku/mobile.png',full_page=True)
 assert not errors,errors
 b.close();print('PASS: board, levels, notes, undo, entry, persistence, erase, hint, pause, switching, reset, completion, mobile overflow; no browser errors')
