import { useState, useCallback } from 'react';

// Window positioning constants
const INITIAL_WINDOW_OFFSET_X = 100;
const INITIAL_WINDOW_OFFSET_Y = 100;
const WINDOW_CASCADE_OFFSET = 30;
const DEFAULT_WINDOW_WIDTH = 800;
const DEFAULT_WINDOW_HEIGHT = 600;

// Window state management hook
// Following BMAD-METHOD: Simple, Testable, Antifragile
export const useWindowManager = () => {
  const [windows, setWindows] = useState([]);

  const openWindow = useCallback((osId, osDefinition) => {
    const newWindow = {
      id: `${osId}-${Date.now()}`,
      osId,
      osDefinition,
      position: { 
        x: INITIAL_WINDOW_OFFSET_X + windows.length * WINDOW_CASCADE_OFFSET, 
        y: INITIAL_WINDOW_OFFSET_Y + windows.length * WINDOW_CASCADE_OFFSET 
      },
      size: { width: DEFAULT_WINDOW_WIDTH, height: DEFAULT_WINDOW_HEIGHT },
      isMinimized: false,
      zIndex: windows.length,
    };
    setWindows((prev) => [...prev, newWindow]);
  }, [windows.length]);

  const closeWindow = useCallback((windowId) => {
    setWindows((prev) => prev.filter((w) => w.id !== windowId));
  }, []);

  const minimizeWindow = useCallback((windowId) => {
    setWindows((prev) =>
      prev.map((w) =>
        w.id === windowId ? { ...w, isMinimized: !w.isMinimized } : w
      )
    );
  }, []);

  const focusWindow = useCallback((windowId) => {
    setWindows((prev) => {
      const maxZ = Math.max(...prev.map((w) => w.zIndex), 0);
      return prev.map((w) =>
        w.id === windowId ? { ...w, zIndex: maxZ + 1 } : w
      );
    });
  }, []);

  const updateWindowPosition = useCallback((windowId, position) => {
    setWindows((prev) =>
      prev.map((w) => (w.id === windowId ? { ...w, position } : w))
    );
  }, []);

  const updateWindowSize = useCallback((windowId, size) => {
    setWindows((prev) =>
      prev.map((w) => (w.id === windowId ? { ...w, size } : w))
    );
  }, []);

  return {
    windows,
    openWindow,
    closeWindow,
    minimizeWindow,
    focusWindow,
    updateWindowPosition,
    updateWindowSize,
  };
};
