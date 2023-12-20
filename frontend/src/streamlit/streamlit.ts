// Safari doesn't support the EventTarget class, so we use a shim.
import { EventTarget } from "event-target-shim"
import { ArrowDataframeProto, ArrowTable } from "./ArrowTable"

/** Data sent in the custom Streamlit render event. */
export interface RenderData {
  args: any
  disabled: boolean
}

/** Messages from Component -> Streamlit */
enum ComponentMessageType {
  COMPONENT_READY = "streamlit:componentReady",
  SET_COMPONENT_VALUE = "streamlit:setComponentValue",
  SET_FRAME_HEIGHT = "streamlit:setFrameHeight",
}

export class Streamlit {
  public static readonly API_VERSION = 1

  public static readonly RENDER_EVENT = "streamlit:render"

  /** Dispatches events received from Streamlit. */
  public static readonly events = new EventTarget()

  private static registeredMessageListener = false
  private static lastFrameHeight?: number
  public static setComponentReady = (): void => {
    if (!Streamlit.registeredMessageListener) {
      // Register for message events if we haven't already
      window.addEventListener("message", Streamlit.onMessageEvent)
      Streamlit.registeredMessageListener = true
    }

    Streamlit.sendBackMsg(ComponentMessageType.COMPONENT_READY, {
      apiVersion: Streamlit.API_VERSION,
    })
  }

  public static setFrameHeight = (height?: number): void => {
    if (height === undefined) {
    
      height = document.body.scrollHeight
    }

    if (height === Streamlit.lastFrameHeight) {
      // Don't bother updating if our height hasn't changed.
      return
    }

    Streamlit.lastFrameHeight = height
    Streamlit.sendBackMsg(ComponentMessageType.SET_FRAME_HEIGHT, { height })
  }

  public static setComponentValue = (value: any): void => {
    Streamlit.sendBackMsg(ComponentMessageType.SET_COMPONENT_VALUE, { value })
  }

  /** Receive a ForwardMsg from the Streamlit app */
  private static onMessageEvent = (event: MessageEvent): void => {
    const type = event.data["type"]
    switch (type) {
      case Streamlit.RENDER_EVENT:
        Streamlit.onRenderMessage(event.data)
        break
    }
  }

  private static onRenderMessage = (data: any): void => {
    let args = data["args"]
    if (args == null) {
      console.error(
        `Got null args in onRenderMessage. This should never happen`
      )
      args = {}
    }

    // Parse our dataframe arguments with arrow, and merge them into our args dict
    const dataframeArgs =
      data["dfs"] && data["dfs"].length > 0
        ? Streamlit.argsDataframeToObject(data["dfs"])
        : {}

    args = {
      ...args,
      ...dataframeArgs,
    }

    const disabled = Boolean(data["disabled"])

    // Dispatch a render event!
    const eventData = { disabled, args }
    const event = new CustomEvent<RenderData>(Streamlit.RENDER_EVENT, {
      detail: eventData,
    })
    Streamlit.events.dispatchEvent(event)
  }

  private static argsDataframeToObject = (
    argsDataframe: ArgsDataframe[]
  ): object => {
    const argsDataframeArrow = argsDataframe.map(
      ({ key, value }: ArgsDataframe) => [key, Streamlit.toArrowTable(value)]
    )
    return Object.fromEntries(argsDataframeArrow)
  }

  private static toArrowTable = (df: ArrowDataframeProto): ArrowTable => {
    const { data, index, columns } = df.data
    return new ArrowTable(data, index, columns)
  }

  /** Post a message to the Streamlit app. */
  private static sendBackMsg = (type: string, data?: any): void => {
    window.parent.postMessage(
      {
        isStreamlitMessage: true,
        type: type,
        ...data,
      },
      "*"
    )
  }
}

interface ArgsDataframe {
  key: string
  value: ArrowDataframeProto
}
